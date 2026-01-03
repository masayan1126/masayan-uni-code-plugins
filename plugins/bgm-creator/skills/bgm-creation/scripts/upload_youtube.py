#!/usr/bin/env python3
"""
YouTube Video Uploader

YouTube Data API v3を使用して動画をアップロードします。
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


# YouTube APIのスコープ
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# リトライ設定
MAX_RETRIES = 3
RETRY_STATUSES = [500, 502, 503, 504]

# 対応する動画フォーマット
VALID_VIDEO_FORMATS = ['.mp4', '.mov', '.avi', '.wmv', '.flv', '.webm', '.mkv']


def save_credentials(creds, token_file):
    """
    認証情報を安全にJSON形式で保存

    Args:
        creds: Credentialsオブジェクト
        token_file: 保存先ファイルパス
    """
    token_data = {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }

    with open(token_file, 'w') as f:
        json.dump(token_data, f)

    # セキュリティのためファイルパーミッションを制限
    os.chmod(token_file, 0o600)


def load_credentials(token_file):
    """
    保存された認証情報をロード

    Args:
        token_file: トークンファイルパス

    Returns:
        Credentialsオブジェクト、存在しない場合はNone
    """
    if not os.path.exists(token_file):
        return None

    try:
        with open(token_file, 'r') as f:
            token_data = json.load(f)

        creds = Credentials(
            token=token_data.get('token'),
            refresh_token=token_data.get('refresh_token'),
            token_uri=token_data.get('token_uri'),
            client_id=token_data.get('client_id'),
            client_secret=token_data.get('client_secret'),
            scopes=token_data.get('scopes')
        )
        return creds
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Warning: Invalid token file format. Re-authentication required.")
        return None


def authenticate(credentials_file='credentials.json', token_file='token.json'):
    """
    YouTube APIの認証を行う

    Args:
        credentials_file: OAuth 2.0クライアント認証情報ファイル
        token_file: 保存されたトークンファイル（JSON形式）

    Returns:
        認証済みのCredentialsオブジェクト
    """
    # セキュリティチェック: credentials.jsonのパーミッション確認
    if os.path.exists(credentials_file):
        stat_info = os.stat(credentials_file)
        if stat_info.st_mode & 0o077:  # 所有者以外が読み取り可能
            print(f"Warning: {credentials_file} has insecure permissions!")
            print("Fixing permissions...")
            os.chmod(credentials_file, 0o600)

    creds = None

    # 既存のトークンをロード
    creds = load_credentials(token_file)

    # トークンが無効または存在しない場合は認証フローを実行
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing access token...")
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"Token refresh failed: {e}")
                print("Re-authentication required.")
                creds = None

        if not creds:
            if not os.path.exists(credentials_file):
                print(f"Error: {credentials_file} not found.")
                print("\nPlease follow these steps:")
                print("1. Go to https://console.cloud.google.com/")
                print("2. Create a new project")
                print("3. Enable YouTube Data API v3")
                print("4. Create OAuth 2.0 credentials (Desktop app)")
                print("5. Download credentials.json")
                print("6. Place it in the project root")
                sys.exit(1)

            print("Starting authentication flow...")
            print("A browser window will open for authentication.")
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # トークンを安全に保存
        save_credentials(creds, token_file)
        print("✓ Authentication successful")

    return creds


def load_metadata(metadata_file):
    """
    メタデータJSONファイルをロード

    Args:
        metadata_file: メタデータファイルパス

    Returns:
        メタデータ辞書
    """
    with open(metadata_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def upload_video(youtube, video_file, metadata):
    """
    動画をYouTubeにアップロード

    Args:
        youtube: YouTube APIクライアント
        video_file: 動画ファイルパス
        metadata: メタデータ辞書

    Returns:
        アップロード結果辞書
    """
    # リクエストボディの作成
    body = {
        'snippet': {
            'title': metadata.get('title', 'Untitled'),
            'description': metadata.get('description', ''),
            'tags': metadata.get('tags', []),
            'categoryId': metadata.get('category', '10')  # 10 = Music
        },
        'status': {
            'privacyStatus': metadata.get('privacy_status', 'public'),
            'selfDeclaredMadeForKids': False
        }
    }

    # メディアファイルの準備
    media = MediaFileUpload(
        video_file,
        chunksize=-1,  # 一度にアップロード
        resumable=True
    )

    # アップロードリクエスト
    print(f"\nUploading: {Path(video_file).name}")
    print(f"Title: {body['snippet']['title'][:80]}..." if len(body['snippet']['title']) > 80 else f"Title: {body['snippet']['title']}")
    print(f"Privacy: {body['status']['privacyStatus']}")
    print("\nThis may take a while depending on file size and network speed...")

    request = youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )

    # プログレス表示付きアップロード（リトライ制御付き）
    response = None
    retry_count = 0

    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                progress = int(status.progress() * 100)
                print(f"Upload progress: {progress}%", end='\r')
        except HttpError as e:
            if e.resp.status in RETRY_STATUSES and retry_count < MAX_RETRIES:
                retry_count += 1
                # Exponential backoff
                wait_time = 2 ** retry_count
                print(f"\nRetryable error ({e.resp.status}). Waiting {wait_time}s before retry {retry_count}/{MAX_RETRIES}...")
                time.sleep(wait_time)
                continue
            else:
                # エラーの詳細をログに記録するが、機密情報は除外
                print(f"\nUpload failed with error code: {e.resp.status}")
                raise

    print("\n")
    return response


def upload_thumbnail(youtube, video_id, thumbnail_file):
    """
    動画のサムネイルをアップロード

    Args:
        youtube: YouTube APIクライアント
        video_id: 動画ID
        thumbnail_file: サムネイル画像ファイルパス

    Returns:
        サムネイルアップロード結果
    """
    print(f"\nUploading thumbnail: {Path(thumbnail_file).name}")

    media = MediaFileUpload(thumbnail_file, mimetype='image/jpeg', resumable=True)

    request = youtube.thumbnails().set(
        videoId=video_id,
        media_body=media
    )

    response = request.execute()
    print("✓ Thumbnail uploaded successfully")

    return response


def main():
    parser = argparse.ArgumentParser(
        description="Upload video to YouTube with metadata"
    )
    parser.add_argument(
        "--video",
        "-v",
        required=True,
        help="Video file to upload"
    )
    parser.add_argument(
        "--metadata",
        "-m",
        help="Metadata JSON file (if not provided, will look for <video>_metadata.json)"
    )
    parser.add_argument(
        "--credentials",
        "-c",
        default="credentials.json",
        help="OAuth credentials file (default: credentials.json)"
    )
    parser.add_argument(
        "--token",
        "-t",
        default="token.json",
        help="Token file (default: token.json)"
    )
    parser.add_argument(
        "--thumbnail",
        "-th",
        help="Thumbnail image file (JPG/PNG, recommended 1280x720). If not provided, will look in outputs/thumbnails/"
    )

    args = parser.parse_args()

    # 動画ファイルの検証
    video_path = Path(args.video)
    if not video_path.exists():
        print(f"Error: Video file not found: {args.video}")
        sys.exit(1)

    if video_path.suffix.lower() not in VALID_VIDEO_FORMATS:
        print(f"Warning: {video_path.suffix} may not be a supported video format")
        print(f"Supported formats: {', '.join(VALID_VIDEO_FORMATS)}")

    # メタデータファイルの決定
    if args.metadata:
        metadata_file = args.metadata
    else:
        # デフォルト: <video>_metadata.json
        metadata_file = video_path.parent / f"{video_path.stem}_metadata.json"

    # メタデータの読み込み
    if not Path(metadata_file).exists():
        print(f"Error: Metadata file not found: {metadata_file}")
        print("\nGenerate metadata first using:")
        print(f"python scripts/generate_metadata.py --video {args.video}")
        sys.exit(1)

    print(f"Loading metadata from: {metadata_file}")
    metadata = load_metadata(metadata_file)

    # 認証
    print("\n=== YouTube API Authentication ===\n")
    try:
        creds = authenticate(args.credentials, args.token)
    except Exception as e:
        print(f"Authentication error: {e}")
        sys.exit(1)

    # YouTube APIクライアントの構築
    youtube = build('youtube', 'v3', credentials=creds)

    # アップロード
    print("\n=== Uploading to YouTube ===\n")
    try:
        response = upload_video(youtube, str(video_path), metadata)

        # 結果表示
        video_id = response['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        print("✓ Upload successful!")
        print(f"\nVideo ID: {video_id}")
        print(f"Video URL: {video_url}")
        print(f"Title: {response['snippet']['title']}")
        print(f"Privacy: {response['status']['privacyStatus']}")
        print()

        # サムネイルのアップロード
        thumbnail_path = None
        if args.thumbnail:
            thumbnail_path = Path(args.thumbnail)
        else:
            # デフォルト: outputs/thumbnails/ から動画名と同じサムネイルを探す
            thumbnails_dir = Path("outputs/thumbnails")
            for ext in ['.jpg', '.jpeg', '.png']:
                potential_thumbnail = thumbnails_dir / f"{video_path.stem}{ext}"
                if potential_thumbnail.exists():
                    thumbnail_path = potential_thumbnail
                    break

        if thumbnail_path and thumbnail_path.exists():
            try:
                upload_thumbnail(youtube, video_id, str(thumbnail_path))
            except HttpError as e:
                print(f"⚠ Warning: Thumbnail upload failed: {e}")
                print("Video was uploaded successfully, but thumbnail could not be set.")
        elif args.thumbnail:
            print(f"⚠ Warning: Thumbnail file not found: {args.thumbnail}")

        # 結果をファイルに保存
        result_file = video_path.parent / f"{video_path.stem}_upload_result.json"
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump({
                'video_id': video_id,
                'video_url': video_url,
                'upload_time': response.get('snippet', {}).get('publishedAt'),
                'title': response['snippet']['title'],
                'privacy_status': response['status']['privacyStatus'],
                'thumbnail_uploaded': thumbnail_path is not None and thumbnail_path.exists()
            }, f, ensure_ascii=False, indent=2)

        print(f"\nUpload result saved to: {result_file}")

    except HttpError as e:
        print(f"\nYouTube API error: {e}")
        if e.resp.status == 403:
            print("\nPossible reasons:")
            print("- API quota exceeded (10,000 units per day)")
            print("- YouTube Data API v3 not enabled")
            print("- Invalid credentials")
        elif e.resp.status == 400:
            print("\nInvalid request. Check your metadata.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
