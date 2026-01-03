#!/usr/bin/env python3
"""
YouTube Metadata Generator

動画ファイル名やジャンルからYouTubeアップロード用のメタデータを生成します。
"""

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path


# YouTube の制限
YOUTUBE_TITLE_MAX_LENGTH = 100
YOUTUBE_DESCRIPTION_MAX_LENGTH = 5000
YOUTUBE_TAGS_MAX_COUNT = 500


# ジャンル別メタデータテンプレート（英語・日本語対応）
GENRE_METADATA = {
    "kouda_teflon_style": {
        "title_en": "Soulful Japanese Hip-Hop R&B Mix",
        "title_ja": "ソウルフル ジャパニーズ ヒップホップ R&B ミックス",
        "title_suffix": "Smooth Urban Beats",
        "description_en": """🎤 Immerse yourself in the smooth world of Japanese Hip-Hop meets R&B! This soulful mix features melodic hooks, atmospheric production, and deep grooves perfect for any mood. Experience the fusion of urban soul with Japanese hip-hop aesthetics.

✨ Features:
- Soulful male vocals with R&B influence
- Fender Rhodes and warm 808 bass
- Minimalist trap drums and atmospheric pads
- Clean, spacious mix with deep bass
- Smooth melodic flow and jazz influences

🎧 Ideal for:
- Work and study sessions
- Relaxing and unwinding
- Driving and commuting
- Creative projects
- Late-night chill vibes

Subscribe for more Japanese Hip-Hop, R&B, and soulful beats!""",
        "description_ja": """🎤 日本のヒップホップとR&Bが融合した、ソウルフルな世界へようこそ！メロディアスなフック、アトモスフェリックなプロダクション、深いグルーヴが特徴的なミックスです。アーバンソウルと日本のヒップホップ美学の融合をお楽しみください。

✨ 特徴:
- R&B的な影響を受けたソウルフルな男性ボーカル
- Fender Rhodesと温かい808ベース
- ミニマルなトラップドラムとアトモスフェリックなパッド
- クリーンでスペーシャスなミックスと深いベース
- スムーズなメロディックフローとジャズの影響

🎧 こんな時におすすめ:
- 作業・勉強用BGM
- リラックス・くつろぎタイム
- ドライブ・通勤時間
- クリエイティブプロジェクト
- 深夜のチルタイム

チャンネル登録で、もっとJapanese Hip-Hop、R&B、ソウルフルなビートをお楽しみください!""",
        "hashtags": "#japaneseHipHop #rnb #soul #bgm #beats #music #chill #hiphop #urban #soulful #workmusic #studymusic #chillbeats #smoothjazz #urbanmusic #ヒップホップ #アールアンドビー #ソウル #作業用BGM #チル音楽",
        "tags": ["japanese hip-hop", "r&b", "soul", "bgm", "beats", "melodic", "urban music", "soulful", "chill", "work music", "study music"],
        "category": "10"  # Music
    },
    "lofi_synth": {
        "title_en": "Nostalgic Lo-Fi Synth Mix",
        "title_ja": "ノスタルジック ローファイ シンセ ミックス",
        "title_suffix": "80s Retro Chillwave",
        "description_en": """🎹 Travel back to the 80s with this nostalgic lo-fi synth mix! Featuring warm analog synthesizers, vintage pads, and cozy retro vibes. Perfect for studying, relaxing, or drifting into peaceful sleep with the comforting sounds of Moog bass and soft arpeggios.

✨ Features:
- Warm analog Moog synthesizers
- Vintage 80s synth pads and textures
- Soft arpeggio patterns
- Tape saturation and vinyl warmth
- Nostalgic retro electronic vibes

🎧 Ideal for:
- Study and concentration
- Work and productivity
- Relaxation and meditation
- Sleep and bedtime
- Nostalgic mood enhancement

Subscribe for more lo-fi, synthwave, and retro electronic music!""",
        "description_ja": """🎹 ノスタルジックなローファイシンセミックスで80年代へタイムスリップ！温かみのあるアナログシンセサイザー、ヴィンテージパッド、心地よいレトロバイブスが特徴です。勉強、リラックス、または穏やかな眠りに最適な、Moogベースとソフトアルペジオの心地よいサウンドです。

✨ 特徴:
- 温かみのあるアナログMoogシンセサイザー
- ヴィンテージ80年代シンセパッドとテクスチャ
- ソフトなアルペジオパターン
- テープサチュレーションとヴィンテージの温かみ
- ノスタルジックなレトロエレクトロニックバイブス

🎧 こんな時におすすめ:
- 勉強・集中作業
- 仕事・生産性向上
- リラックス・瞑想
- 睡眠・就寝前
- ノスタルジックな気分を味わいたい時

チャンネル登録で、もっとローファイ、シンセウェーブ、レトロエレクトロニックミュージックをお楽しみください!""",
        "hashtags": "#lofi #synth #80s #studymusic #relaxing #chillwave #electronic #bgm #nostalgic #vintage #retrowave #sleepmusic #workmusic #moog #analogsynth #ローファイ #シンセ #80年代 #作業用BGM #リラックス音楽",
        "tags": ["lofi", "synth", "80s", "study music", "relaxing", "nostalgic", "electronic", "chillwave", "retro", "vintage", "sleep music"],
        "category": "10"
    },
    "chillout": {
        "title_template": "Chillout Mix | {} | Ambient Relaxation Music",
        "description_template": """【概要】
深いリラクゼーションのためのアンビエント・チルアウトミュージックです。

【こんな時にオススメ】
✓ 瞑想・ヨガ
✓ 睡眠前のリラックス
✓ スパ・マッサージ

【ジャンル】
Chillout, Ambient, Meditation, Relaxation

---
#chillout #ambient #relaxing #meditation #sleepmusic #peaceful #bgm""",
        "tags": ["chillout", "ambient", "relaxing", "meditation", "peaceful", "sleep music", "spa"],
        "category": "10"
    },
    "synthwave": {
        "title_template": "Synthwave Mix | {} | Retro 80s Cyberpunk Vibes",
        "description_template": """【概要】
レトロな80年代サウンドとサイバーパンクの雰囲気を持つシンセウェーブミックスです。

【こんな時にオススメ】
✓ ドライブミュージック
✓ ゲーム・作業用BGM
✓ トレーニング

【ジャンル】
Synthwave, Retrowave, 80s, Electronic, Cyberpunk

---
#synthwave #retrowave #80s #cyberpunk #electronic #neon #bgm #retro""",
        "tags": ["synthwave", "retrowave", "80s", "cyberpunk", "electronic", "retro", "neon", "outrun"],
        "category": "10"
    },
    "vaporwave": {
        "title_en": "Dreamy Vaporwave Aesthetic Mix",
        "title_ja": "ドリーミー ヴェイパーウェーブ エステティック ミックス",
        "title_suffix": "Nostalgic Mall Music Vibes",
        "description_en": """🌸 Drift into the dreamy world of Vaporwave aesthetics! This nostalgic mix features slowed samples, reverb-soaked synths, and pitch-shifted vocals that capture the essence of 90s mall culture and retro Japanese city pop. Perfect for late-night relaxation and creative inspiration.

✨ Features:
- Slowed and pitch-shifted vocal samples
- Reverb-drenched synthesizers and Rhodes piano
- Dreamy nostalgic mall music aesthetic
- VHS tape distortion and glitch effects
- Lo-fi texture with retro commercial jingles
- Floating ambient atmosphere

🎧 Ideal for:
- Late-night study and work sessions
- Artistic and creative projects
- Relaxation and meditation
- Nostalgic mood enhancement
- Background music for art streaming
- Chill evening vibes

Subscribe for more Vaporwave, Lo-Fi, and aesthetic music!""",
        "description_ja": """🌸 ヴェイパーウェーブの夢幻的な世界へようこそ！90年代のモールカルチャーとレトロな日本のシティポップのエッセンスを捉えた、ノスタルジックなミックスです。スローダウンされたサンプル、リバーブたっぷりのシンセ、ピッチシフトされたボーカルが特徴的です。深夜のリラックスとクリエイティブなインスピレーションに最適。

✨ 特徴:
- スローダウン＆ピッチシフトされたボーカルサンプル
- リバーブたっぷりのシンセサイザーとローズピアノ
- 夢のような懐かしいモール音楽美学
- VHSテープの歪みとグリッチエフェクト
- レトロCMジングル入りのローファイテクスチャ
- 浮遊するアンビエント雰囲気

🎧 こんな時におすすめ:
- 深夜の勉強・作業用BGM
- アート・クリエイティブプロジェクト
- リラックス・瞑想
- ノスタルジックな気分を味わいたい時
- アート配信の背景音楽
- チルな夜のムード作り

チャンネル登録で、もっとVaporwave、Lo-Fi、エステティック音楽をお楽しみください!""",
        "hashtags": "#vaporwave #aesthetic #lofi #dreamy #mallmusic #nostalgia #chillwave #bgm #studymusic #relaxing #glitch #retrowave #japaneseaesthetic #ambientmusic #chillvibes #ヴェイパーウェーブ #エステティック #ローファイ #作業用BGM #リラックス音楽",
        "tags": ["vaporwave", "aesthetic", "lofi", "dreamy", "experimental", "nostalgia", "retro", "chill", "ambient", "study music", "relaxing"],
        "category": "10"
    },
    "cyberpunk_rnb": {
        "title_template": "Cyberpunk R&B Mix | {} | Future Soul Vibes",
        "description_template": """【概要】
未来的なサウンドとR&Bソウルを融合させたサイバーパンクミュージックです。

【こんな時にオススメ】
✓ 作業用BGM
✓ ナイトドライブ
✓ クリエイティブワーク

【ジャンル】
Cyberpunk, Alternative R&B, Electronic Soul, Future Bass

---
#cyberpunk #rnb #electronic #soul #futuristic #alternative #bgm""",
        "tags": ["cyberpunk", "r&b", "alternative", "electronic", "soul", "futuristic", "dark"],
        "category": "10"
    },
    "electro_pop": {
        "title_template": "Electro Pop Mix | {} | Upbeat Electronic Music",
        "description_template": """【概要】
キャッチーでアップビートなエレクトロポップミュージックです。

【こんな時にオススメ】
✓ トレーニング
✓ パーティー
✓ 気分転換

【ジャンル】
Electro Pop, Electronic, Dance, Pop

---
#electropop #electronic #pop #dance #upbeat #catchy #energetic #bgm""",
        "tags": ["electro pop", "electronic", "pop", "dance", "upbeat", "catchy", "energetic"],
        "category": "10"
    },
    "hood_rap": {
        "title_template": "Hood Rap Mix | {} | Street Hip Hop Beats",
        "description_template": """【概要】
本格的なストリートヒップホップとフッドラップのビートミックスです。

【こんな時にオススメ】
✓ トレーニング
✓ ドライブミュージック
✓ パーティー

【ジャンル】
Hood Rap, Hip-Hop, Street Music, Underground

---
#hoodrap #hiphop #streetmusic #underground #rap #beats #urban #bgm""",
        "tags": ["hood rap", "hip-hop", "street music", "underground", "rap", "beats", "urban"],
        "category": "10"
    },
    "gangster_trap": {
        "title_template": "Gangster Trap Mix | {} | Hard Hip Hop Beats",
        "description_template": """【概要】
ハードヒッティングな808とダークな雰囲気のギャングスタトラップミュージックです。

【こんな時にオススメ】
✓ トレーニング
✓ ゲーム用BGM
✓ モチベーションアップ

【ジャンル】
Trap, Gangster Rap, Hip-Hop, Bass Music

---
#trap #gangsterrap #hiphop #808 #hard #beats #dark #bgm""",
        "tags": ["trap", "gangster rap", "hip-hop", "808", "hard", "beats", "dark", "aggressive"],
        "category": "10"
    },
    "spoken_rap": {
        "title_template": "Spoken Word Rap | {} | Narrative Hip Hop",
        "description_template": """【概要】
ストーリーテリングに焦点を当てたスポークンワードラップです。

【こんな時にオススメ】
✓ 集中したいとき
✓ 詩的な雰囲気を楽しみたいとき
✓ リラックスタイム

【ジャンル】
Spoken Word, Rap, Narrative Hip-Hop, Poetry

---
#spokenword #rap #narrative #poetry #hiphop #storytelling #bgm""",
        "tags": ["spoken word", "rap", "narrative", "poetry", "hip-hop", "storytelling", "minimal"],
        "category": "10"
    }
}


def detect_genre_from_filename(filename):
    """
    ファイル名からジャンルを推測

    Args:
        filename: ファイル名

    Returns:
        推測されたジャンルキー（見つからない場合はNone）
    """
    filename_lower = filename.lower()

    # ジャンルキーワードマッピング
    genre_keywords = {
        "kouda_teflon_style": ["kouda", "teflon", "jpn", "japanese", "jhiphop"],
        "lofi_synth": ["lofi", "lo-fi", "synth"],
        "chillout": ["chill", "chillout", "ambient"],
        "synthwave": ["synthwave", "retro", "80s"],
        "vaporwave": ["vapor", "vaporwave", "aesthetic"],
        "cyberpunk_rnb": ["cyberpunk", "cyber", "rnb"],
        "electro_pop": ["electro", "pop"],
        "hood_rap": ["hood", "street"],
        "gangster_trap": ["gangster", "trap"],
        "spoken_rap": ["spoken", "narrative"]
    }

    for genre_key, keywords in genre_keywords.items():
        for keyword in keywords:
            if keyword in filename_lower:
                return genre_key

    return None


def sanitize_text(text, max_length=None):
    """
    テキストをサニタイズ

    Args:
        text: サニタイズするテキスト
        max_length: 最大長（Noneの場合は制限なし）

    Returns:
        サニタイズされたテキスト
    """
    if text is None:
        return ""

    # 制御文字の除去（改行、タブ以外）
    text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t')

    # 長さ制限
    if max_length and len(text) > max_length:
        text = text[:max_length]

    return text


def validate_privacy_status(privacy_status):
    """
    プライバシーステータスのバリデーション

    Args:
        privacy_status: プライバシーステータス

    Returns:
        検証済みのプライバシーステータス

    Raises:
        ValueError: 無効な値の場合
    """
    valid_statuses = ['public', 'unlisted', 'private']
    if privacy_status not in valid_statuses:
        raise ValueError(f"Invalid privacy status: {privacy_status}. Must be one of {valid_statuses}")
    return privacy_status


def generate_metadata(genre_key, title_suffix=None, privacy_status="public"):
    """
    指定されたジャンルのメタデータを生成（英語→日本語の順）

    Args:
        genre_key: ジャンルキー
        title_suffix: タイトルのサフィックス（日付など）
        privacy_status: 公開設定（public, unlisted, private）

    Returns:
        メタデータ辞書
    """
    # プライバシーステータスの検証
    privacy_status = validate_privacy_status(privacy_status)

    # title_suffixのサニタイゼーション
    if title_suffix:
        title_suffix = sanitize_text(title_suffix, max_length=50)

    if genre_key not in GENRE_METADATA:
        # デフォルトメタデータ
        return {
            "title": f"BGM Mix {title_suffix or ''}",
            "description": "Background music mix.\n\n#bgm #music",
            "tags": ["bgm", "music"],
            "category": "10",
            "privacy_status": privacy_status
        }

    template = GENRE_METADATA[genre_key]

    # タイトル: English Title | カタカナ日本語 - Suffix
    if "title_en" in template and "title_ja" in template:
        suffix = template.get("title_suffix", "")
        if suffix:
            title = f"{template['title_en']} | {template['title_ja']} - {suffix}"
        else:
            title = f"{template['title_en']} | {template['title_ja']}"
    else:
        # 旧形式の互換性
        suffix = title_suffix or datetime.now().strftime("%Y.%m.%d")
        title = template.get("title_template", "BGM Mix").format(suffix) if "title_template" in template else "BGM Mix"

    # 説明: 英語説明 + 日本語説明 + ハッシュタグ
    if "description_en" in template and "description_ja" in template:
        description = f"{template['description_en']}\n\n---\n\n{template['description_ja']}\n\n{template.get('hashtags', '#bgm #music')}"
    else:
        # 旧形式の互換性
        description = template.get("description_template", "Background music mix.\n\n#bgm #music")

    # タイトルと説明のサニタイゼーション・バリデーション
    title = sanitize_text(title, max_length=YOUTUBE_TITLE_MAX_LENGTH)
    description = sanitize_text(description, max_length=YOUTUBE_DESCRIPTION_MAX_LENGTH)

    # タグの検証
    tags = template.get("tags", [])
    if len(tags) > YOUTUBE_TAGS_MAX_COUNT:
        tags = tags[:YOUTUBE_TAGS_MAX_COUNT]

    return {
        "title": title,
        "description": description,
        "tags": tags,
        "category": template.get("category", "10"),
        "privacy_status": privacy_status
    }


def save_metadata(metadata, output_file):
    """
    メタデータをJSONファイルに保存

    Args:
        metadata: メタデータ辞書
        output_file: 出力ファイルパス
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Generate YouTube metadata from video file or genre"
    )
    parser.add_argument(
        "--video",
        "-v",
        help="Video file path (genre will be detected from filename)"
    )
    parser.add_argument(
        "--genre",
        "-g",
        help="Genre key (overrides auto-detection)"
    )
    parser.add_argument(
        "--title-suffix",
        "-t",
        help="Title suffix (default: current date)"
    )
    parser.add_argument(
        "--privacy",
        "-p",
        choices=["public", "unlisted", "private"],
        default="public",
        help="Privacy status (default: public)"
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output JSON file (default: derived from video filename)"
    )

    args = parser.parse_args()

    # ジャンルの決定
    genre_key = args.genre
    if not genre_key and args.video:
        # ファイル名から推測
        video_filename = Path(args.video).stem
        genre_key = detect_genre_from_filename(video_filename)
        if genre_key:
            print(f"Detected genre: {genre_key}")
        else:
            print("Warning: Could not detect genre from filename. Using default metadata.")

    # メタデータ生成
    metadata = generate_metadata(
        genre_key or "unknown",
        title_suffix=args.title_suffix,
        privacy_status=args.privacy
    )

    # メタデータ表示
    print("\n=== Generated Metadata ===\n")
    print(f"Title: {metadata['title']}")
    print(f"\nDescription:\n{metadata['description']}")
    print(f"\nTags: {', '.join(metadata['tags'])}")
    print(f"Category: {metadata['category']}")
    print(f"Privacy: {metadata['privacy_status']}")
    print()

    # 出力ファイル名の決定
    if args.output:
        output_file = args.output
    elif args.video:
        video_path = Path(args.video)
        output_file = video_path.parent / f"{video_path.stem}_metadata.json"
    else:
        output_file = "metadata.json"

    # ファイル保存
    save_metadata(metadata, output_file)
    print(f"✓ Saved to: {output_file}\n")


if __name__ == "__main__":
    main()
