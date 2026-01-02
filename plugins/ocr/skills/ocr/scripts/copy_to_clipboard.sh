#!/bin/bash

# 画像から抽出したテキストをクリップボードにコピー
# 使い方: echo "テキスト" | ./copy_to_clipboard.sh

cat | pbcopy
echo "✓ テキストをクリップボードにコピーしました"
