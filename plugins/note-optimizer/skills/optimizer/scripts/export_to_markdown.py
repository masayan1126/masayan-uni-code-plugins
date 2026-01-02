#!/usr/bin/env python3
"""
note記事用Markdownエクスポートスクリプト

noteにインポート可能なMarkdown形式で記事を出力します。
"""

import argparse
import os
from datetime import datetime


def export_to_note_markdown(input_file, output_dir=None, add_metadata=True):
    """
    記事をnote用Markdownとしてエクスポート

    Args:
        input_file: 入力Markdownファイルパス
        output_dir: 出力ディレクトリ（Noneの場合はnote/2_optimized）
        add_metadata: メタデータを追加するか

    Returns:
        出力ファイルパス
    """
    # デフォルト出力ディレクトリ
    if output_dir is None:
        output_dir = "note/2_optimized"

    # 出力ディレクトリを作成
    os.makedirs(output_dir, exist_ok=True)

    # ファイルを読み込み
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 出力ファイル名を生成
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"{base_name}_note_{timestamp}.md")

    # note用の形式に変換
    note_content = convert_to_note_format(content, add_metadata)

    # ファイルに書き込み
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(note_content)

    return output_file


def convert_to_note_format(content, add_metadata=True):
    """
    MarkdownをNote形式に変換

    Args:
        content: 元のMarkdownコンテンツ
        add_metadata: メタデータを追加するか

    Returns:
        note用Markdownコンテンツ
    """
    lines = content.split('\n')
    note_lines = []

    if add_metadata:
        # note用のメタデータコメント（任意）
        note_lines.append('<!-- note用エクスポート -->')
        note_lines.append(f'<!-- 生成日時: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -->')
        note_lines.append('')

    # コンテンツをそのまま追加
    # noteは基本的なMarkdownをサポートしているため、特別な変換は不要
    note_lines.extend(lines)

    return '\n'.join(note_lines)


def main():
    parser = argparse.ArgumentParser(
        description='note記事用Markdownエクスポートツール'
    )
    parser.add_argument(
        'input_file',
        help='入力Markdownファイル'
    )
    parser.add_argument(
        '-o', '--output-dir',
        help='出力ディレクトリ（デフォルト: note/2_optimized）'
    )
    parser.add_argument(
        '--no-metadata',
        action='store_true',
        help='メタデータを追加しない'
    )

    args = parser.parse_args()

    try:
        output_file = export_to_note_markdown(
            args.input_file,
            args.output_dir,
            add_metadata=not args.no_metadata
        )
        print(f"✓ エクスポート完了: {output_file}")
        print(f"\n次のステップ:")
        print(f"1. noteにログイン: https://note.com/")
        print(f"2. 「投稿」→「テキスト」を選択")
        print(f"3. エディタに {output_file} の内容をコピー&ペースト")
        print(f"4. タイトルと見出し画像を設定")
        print(f"5. 「公開する」または「下書き保存」")

    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません: {args.input_file}")
        return 1
    except Exception as e:
        print(f"エラー: {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
