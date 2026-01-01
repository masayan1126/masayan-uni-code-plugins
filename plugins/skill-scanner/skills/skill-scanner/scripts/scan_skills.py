#!/usr/bin/env python3
"""
Scan and list registered Claude agent skills from user and project directories.
Read-only operation - no files are modified.
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import Optional


# Default skill locations on Mac
USER_SKILLS_DIR = Path.home() / ".claude" / "skills"
GIT_PROJECTS_DIR = Path.home() / "git"


def parse_frontmatter(skill_md_path: Path) -> Optional[dict]:
    """Parse YAML frontmatter from SKILL.md file (without yaml dependency)."""
    try:
        with open(skill_md_path, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            # No frontmatter, try to extract from first heading and paragraph
            lines = content.strip().split("\n")
            name = None
            description = None
            for line in lines:
                if line.startswith("# ") and not name:
                    name = line[2:].strip()
                elif line.strip() and not line.startswith("#") and not description:
                    description = line.strip()
                    break
            return {"name": name, "description": description}

        # Find the closing ---
        end_idx = content.find("---", 3)
        if end_idx == -1:
            return None

        yaml_content = content[3:end_idx].strip()

        # Simple YAML parsing without external dependency
        result = {}
        for line in yaml_content.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                result[key] = value

        return result
    except Exception as e:
        return {"error": str(e)}


def check_additional_files(skill_dir: Path) -> list[str]:
    """Check for additional reference files in skill directory."""
    ref_files = []
    known_patterns = ["REFERENCE", "PROCEDURE", "SCHEMA", "STYLE", "FORMS", "README"]

    for item in skill_dir.iterdir():
        if item.is_file() and item.suffix == ".md" and item.name != "SKILL.md":
            ref_files.append(item.name)

    return ref_files


def find_skills(search_path: Path) -> list[dict]:
    """Find all skills in the given directory (read-only)."""
    skills = []

    if not search_path.exists():
        return skills

    # Look for SKILL.md files
    for skill_dir in search_path.iterdir():
        if skill_dir.is_dir():
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                meta = parse_frontmatter(skill_md) or {}
                ref_files = check_additional_files(skill_dir)

                skills.append({
                    "name": meta.get("name", skill_dir.name),
                    "description": meta.get("description", "No description"),
                    "path": str(skill_dir),
                    "has_scripts": (skill_dir / "scripts").exists(),
                    "has_references": len(ref_files) > 0,
                    "ref_files": ref_files,
                    "has_assets": (skill_dir / "assets").exists(),
                })

    return skills


def find_project_skills(git_dir: Path, max_depth: int = 3) -> dict[str, list[dict]]:
    """
    Scan all projects in ~/git for .claude/skills directories (read-only).
    Supports monorepo structures by scanning subdirectories recursively.

    Args:
        git_dir: The git projects directory (e.g., ~/git)
        max_depth: Maximum depth to search for .claude/skills (default: 3)
    """
    results = {}

    if not git_dir.exists():
        return results

    def scan_directory(base_path: Path, current_depth: int = 0):
        """Recursively scan for .claude/skills directories."""
        if current_depth > max_depth:
            return

        try:
            for item in base_path.iterdir():
                if not item.is_dir():
                    continue

                # Skip hidden directories (except .claude)
                if item.name.startswith(".") and item.name != ".claude":
                    continue

                # Check if this directory has .claude/skills
                skills_path = item / ".claude" / "skills"
                if skills_path.exists():
                    skills = find_skills(skills_path)
                    if skills:
                        results[str(skills_path)] = skills

                # Recurse into subdirectories (for monorepo support)
                if current_depth < max_depth:
                    scan_directory(item, current_depth + 1)
        except PermissionError:
            pass  # Skip directories we can't access

    scan_directory(git_dir)
    return results


def scan_all_locations(include_git_projects: bool = False, custom_paths: list[str] = None) -> dict[str, list[dict]]:
    """Scan all locations for skills (read-only operation)."""
    results = {}

    if custom_paths:
        # Custom paths only
        for p in custom_paths:
            path = Path(p).expanduser()
            skills = find_skills(path)
            results[str(path)] = skills
    else:
        # Default: always scan user-level skills
        user_skills = find_skills(USER_SKILLS_DIR)
        results[str(USER_SKILLS_DIR)] = user_skills

        # Optionally scan ~/git projects
        if include_git_projects:
            project_results = find_project_skills(GIT_PROJECTS_DIR)
            results.update(project_results)

    return results


def format_output(results: dict[str, list[dict]], format_type: str = "text") -> str:
    """Format scan results for display."""
    if format_type == "json":
        return json.dumps(results, indent=2, ensure_ascii=False)

    # Text format
    lines = []
    total_skills = 0
    locations_with_skills = 0

    for location, skills in results.items():
        if skills:
            locations_with_skills += 1
            lines.append(f"\n📁 {location}")
            for skill in skills:
                total_skills += 1
                extras = []
                if skill["has_scripts"]:
                    extras.append("scripts")
                if skill["has_references"]:
                    extras.append(f"refs: {', '.join(skill['ref_files'])}")
                if skill["has_assets"]:
                    extras.append("assets")
                extras_str = f" [{', '.join(extras)}]" if extras else ""

                lines.append(f"   • {skill['name']}{extras_str}")
                desc = skill['description'] or "No description"
                lines.append(f"     {desc[:80]}{'...' if len(desc) > 80 else ''}")

    header = f"🔍 Found {total_skills} skill(s) in {locations_with_skills} location(s)"
    lines.insert(0, header)

    if total_skills == 0:
        lines.append("\n(No skills found)")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Scan for registered Claude agent skills (read-only)"
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Custom paths to scan"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output in JSON format"
    )
    parser.add_argument(
        "--git-projects",
        action="store_true",
        help="Also scan ~/git/*/.claude/skills for project-level skills"
    )

    args = parser.parse_args()

    custom_paths = args.paths if args.paths else None

    results = scan_all_locations(
        include_git_projects=args.git_projects,
        custom_paths=custom_paths
    )
    output = format_output(results, "json" if args.json else "text")
    print(output)


if __name__ == "__main__":
    main()
