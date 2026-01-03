#!/usr/bin/env python3
"""
BGM Prompt Generator for Suno

このスクリプトは、ジャンルに基づいてSuno用のBGMプロンプトを生成します。
"""

import argparse
import json
import os
import random
import re
from datetime import datetime
from pathlib import Path


# ジャンル定義（Suno最適化版）
# - 200文字以内
# - BPM、キー、具体的な楽器名を明示
# - 簡潔で明確な表現
GENRES = {
    "kouda_teflon_style": {
        "name": "鋼田テフロン風",
        "bpm": "85-95",
        "key": "C minor",
        "template": "Japanese Hip-Hop + R&B, 90 BPM, C minor, soulful male vocals, warm Fender Rhodes electric piano, deep Roland TR-808 bass, minimalist trap drums, atmospheric synth pads, smooth melodic flow",
        "tags": ["japanese-hip-hop", "r&b", "soul", "melodic", "urban"],
        "variations": [
            "jazzy guitar riffs",
            "vinyl scratches texture",
            "lo-fi tape saturation",
            "reverb-drenched vocals",
            "mellow saxophone accents"
        ]
    },
    "lofi_synth": {
        "name": "Lo-Fi Synth",
        "bpm": "70-80",
        "key": "A minor",
        "template": "Lo-Fi + Synthwave, 75 BPM, A minor, warm Moog synthesizer, vintage analog pads, soft arpeggiator sequence, tape saturation, vinyl crackle texture, nostalgic 80s cozy vibe",
        "tags": ["lo-fi", "synth", "80s", "nostalgic", "electronic", "chill"],
        "variations": [
            "Yamaha DX7 electric piano layers",
            "gentle filter sweeps",
            "ambient noise bed",
            "soft reverb tail",
            "retro drum machine"
        ]
    },
    "chillout": {
        "name": "Chillout",
        "bpm": "60-75",
        "key": "G major",
        "template": "Ambient + Chillout, 65 BPM, G major, soft acoustic piano, warm bass guitar, gentle brushed drums, ethereal synth pad layers, peaceful meditation vibe, calm spa atmosphere",
        "tags": ["chillout", "ambient", "relaxing", "peaceful", "meditation"],
        "variations": [
            "nature sounds ambience",
            "soft string ensemble",
            "wind chimes texture",
            "ocean waves background",
            "flute melodies"
        ]
    },
    "synthwave": {
        "name": "Synthwave",
        "bpm": "110-125",
        "key": "D minor",
        "template": "Synthwave + Retrowave, 120 BPM, D minor, bright Juno-106 synth lead, gated reverb snare drum, pulsing Moog bass, lush arpeggiator sequence, neon 80s cyberpunk atmosphere",
        "tags": ["synthwave", "80s", "retro", "electronic", "cyberpunk"],
        "variations": [
            "sidechain compression pumping",
            "cinematic string sections",
            "vocoder vocal effects",
            "epic cinematic build-up",
            "analog delay trails"
        ]
    },
    "vaporwave": {
        "name": "Vaporwave",
        "bpm": "60-70",
        "key": "E major",
        "template": "Vaporwave + Lo-Fi, 65 BPM, E major, slowed pitched samples, reverb-soaked synthesizers, dreamy Rhodes electric piano, pitch-shifted vocals, nostalgic mall music aesthetic",
        "tags": ["vaporwave", "lo-fi", "nostalgic", "dreamy", "aesthetic"],
        "variations": [
            "glitch effects processing",
            "VHS tape distortion",
            "retro commercial jingles",
            "floating ambient atmosphere",
            "chopped vocal samples"
        ]
    },
    "cyberpunk_rnb": {
        "name": "Cyberpunk R&B",
        "bpm": "80-95",
        "key": "F# minor",
        "template": "Alternative R&B + Cyberpunk, 85 BPM, F# minor, smooth silky vocals, atmospheric synthesizers, deep sub bass, glitch effects, futuristic electronic soul vibe, dystopian mood",
        "tags": ["cyberpunk", "r&b", "alternative", "electronic", "soul", "futuristic"],
        "variations": [
            "vocoder vocal harmonies",
            "industrial metallic percussion",
            "dark ambient pad layers",
            "future bass drop elements",
            "robotic vocal chops"
        ]
    },
    "electro_pop": {
        "name": "Electro Pop",
        "bpm": "120-130",
        "key": "C major",
        "template": "Electro Pop + Dance, 125 BPM, C major, bright Moog synthesizer leads, punchy Roland TR-808 drum machine, catchy vocal hooks, side-chain compressed bass, upbeat energetic party vibe",
        "tags": ["electro-pop", "pop", "electronic", "catchy", "dance"],
        "variations": [
            "chopped vocal samples",
            "clap samples layers",
            "sweep riser effects",
            "buildup drop section",
            "4-on-the-floor kick pattern"
        ]
    },
    "hood_rap": {
        "name": "Hood Rap",
        "bpm": "85-95",
        "key": "G minor",
        "template": "Hood Rap + Street Hip-Hop, 90 BPM, G minor, heavy Roland TR-808 sub bass, vinyl turntable scratching, gritty breakbeat drums, raw street atmosphere, authentic underground flow",
        "tags": ["hood-rap", "hip-hop", "street", "scratching", "ghetto-rap", "underground"],
        "variations": [
            "DJ turntable scratch effects",
            "distant police siren samples",
            "chopped soul samples",
            "aggressive vocal delivery",
            "lo-fi dusty texture"
        ]
    },
    "gangster_trap": {
        "name": "Gangster Trap",
        "bpm": "130-150",
        "key": "B minor",
        "template": "Trap + Gangster Rap, 140 BPM, B minor, booming Roland TR-808 bass kicks, rapid hi-hat rolls, dark menacing piano stabs, ominous synth lead, hard aggressive energy",
        "tags": ["trap", "gangster-rap", "hip-hop", "hard", "aggressive"],
        "variations": [
            "triple-time hi-hat patterns",
            "brass orchestral hits",
            "sub bass drops",
            "eerie haunting melody",
            "snare drum rolls"
        ]
    },
    "spoken_rap": {
        "name": "Spoken Rap",
        "bpm": "80-95",
        "key": "A minor",
        "template": "Spoken Word + Hip-Hop, 85 BPM, A minor, intimate narrative storytelling, minimal jazz piano chords, subtle soft brushed drums, upright double bass, conversational poetic flow",
        "tags": ["spoken-word", "rap", "narrative", "jazz", "poetry"],
        "variations": [
            "soft string quartet",
            "ambient atmospheric texture",
            "poetry spoken rhythm",
            "close proximity mic vocal",
            "vinyl static background"
        ]
    }
}


def list_genres():
    """利用可能なジャンルを一覧表示"""
    print("\n=== Available Genres (Suno Optimized) ===\n")
    for i, (key, info) in enumerate(GENRES.items(), 1):
        print(f"{i}. {key}")
        print(f"   Name: {info['name']}")
        print(f"   BPM: {info['bpm']} | Key: {info['key']}")
        print(f"   Tags: {', '.join(info['tags'])}")
        print()


def generate_prompt(genre_key, add_variation=True, custom_elements=None):
    """
    指定されたジャンルのプロンプトを生成

    Args:
        genre_key: ジャンルキー
        add_variation: バリエーション要素を追加するか
        custom_elements: カスタム要素のリスト

    Returns:
        生成されたプロンプト文字列
    """
    if genre_key not in GENRES:
        raise ValueError(f"Unknown genre: {genre_key}")

    genre = GENRES[genre_key]
    prompt = genre["template"]

    # バリエーション追加（200文字制限を考慮）
    if add_variation and genre.get("variations"):
        variation = random.choice(genre["variations"])
        test_prompt = f"{prompt}, {variation}"
        if len(test_prompt) <= 200:
            prompt = test_prompt
        else:
            print(f"⚠ Warning: Variation skipped to keep within 200 char limit")

    # カスタム要素追加（200文字制限を考慮）
    if custom_elements:
        for element in custom_elements:
            test_prompt = f"{prompt}, {element}"
            if len(test_prompt) <= 200:
                prompt = test_prompt
            else:
                print(f"⚠ Warning: Custom element '{element}' skipped to keep within 200 char limit")

    return prompt


def sanitize_filename(filename):
    """
    ファイル名を安全な形式にサニタイズ

    Args:
        filename: サニタイズするファイル名

    Returns:
        安全なファイル名
    """
    # 英数字、アンダースコア、ハイフンのみを許可
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', filename)
    # 連続するアンダースコアを1つに
    safe_name = re.sub(r'_+', '_', safe_name)
    # 先頭と末尾のアンダースコアを除去
    safe_name = safe_name.strip('_')
    # 空文字列の場合はデフォルト値
    return safe_name if safe_name else 'untitled'


def validate_output_path(output_dir):
    """
    出力ディレクトリパスを検証し、パストラバーサルを防止

    Args:
        output_dir: 検証する出力ディレクトリ

    Returns:
        検証済みのPathオブジェクト

    Raises:
        ValueError: 無効なパスの場合
    """
    output_path = Path(output_dir).resolve()
    base_path = Path.cwd().resolve()

    # ベースディレクトリ外への書き込みを防止
    if not str(output_path).startswith(str(base_path)):
        raise ValueError(f"Invalid output directory: path traversal detected ({output_dir})")

    return output_path


def save_prompt(prompt, genre_key, output_dir):
    """
    生成されたプロンプトをファイルに保存

    Args:
        prompt: プロンプト文字列
        genre_key: ジャンルキー
        output_dir: 出力ディレクトリ

    Returns:
        保存されたファイルパス
    """
    # パストラバーサル対策
    output_path = validate_output_path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # ファイル名のサニタイゼーション
    safe_genre_key = sanitize_filename(genre_key)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_genre_key}_{timestamp}.txt"
    filepath = output_path / filename

    genre = GENRES[genre_key]
    char_count = len(prompt)

    # プロンプトとメタデータを保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Genre: {genre['name']}\n")
        f.write(f"BPM: {genre['bpm']} | Key: {genre['key']}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Character Count: {char_count}/200\n")
        f.write(f"Tags: {', '.join(genre['tags'])}\n")
        f.write("\n--- Suno Prompt (Style of Music) ---\n\n")
        f.write(prompt)
        f.write("\n\n")
        f.write("--- Usage ---\n")
        f.write("1. Go to https://suno.ai/\n")
        f.write("2. Click 'Create' and select 'Custom Mode'\n")
        f.write("3. In 'Style of Music' field, paste the prompt above\n")
        f.write("4. (Optional) Add your lyrics in 'Lyrics' field\n")
        f.write("5. Click 'Create' to generate your BGM\n")

    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Generate BGM prompts for Suno"
    )
    parser.add_argument(
        "--genre",
        "-g",
        help="Genre key (use --list to see available genres)"
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List available genres"
    )
    parser.add_argument(
        "--output",
        "-o",
        default="outputs/prompts",
        help="Output directory (default: outputs/prompts)"
    )
    parser.add_argument(
        "--no-variation",
        action="store_true",
        help="Don't add random variations"
    )
    parser.add_argument(
        "--custom",
        "-c",
        nargs="+",
        help="Add custom elements to the prompt"
    )

    args = parser.parse_args()

    if args.list:
        list_genres()
        return

    if not args.genre:
        print("Error: --genre is required (or use --list to see available genres)")
        parser.print_help()
        return

    try:
        genre = GENRES[args.genre]

        # プロンプト生成
        prompt = generate_prompt(
            args.genre,
            add_variation=not args.no_variation,
            custom_elements=args.custom
        )

        char_count = len(prompt)
        char_status = "✓" if char_count <= 200 else "⚠"

        # プロンプト表示
        print(f"\n=== Generated Suno Prompt for {genre['name']} ===\n")
        print(f"BPM: {genre['bpm']} | Key: {genre['key']}")
        print(f"Character Count: {char_count}/200 {char_status}\n")
        print(f"--- Prompt ---")
        print(prompt)
        print()

        # ファイル保存
        filepath = save_prompt(prompt, args.genre, args.output)
        print(f"✓ Saved to: {filepath}\n")

        # 使用方法の提示
        print("Next steps:")
        print("1. Copy the prompt above")
        print("2. Go to https://suno.ai/")
        print("3. Click 'Create' → 'Custom Mode'")
        print("4. Paste the prompt in 'Style of Music' field")
        print("5. Click 'Create' to generate your BGM")
        print("6. Download the generated audio")
        print("7. Create your video with the audio")
        print("8. Place the video in outputs/videos/")
        print("9. Run generate_metadata.py and upload_youtube.py")
        print()

    except ValueError as e:
        print(f"Error: {e}")
        print("\nUse --list to see available genres")


if __name__ == "__main__":
    main()
