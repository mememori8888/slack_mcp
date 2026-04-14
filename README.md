# YouTube Research AI Agent for Slack

本プロジェクトは、**FastAPI**、**Google Gemini 2.0/1.5**、および **YouTube Data API v3** を統合した、次世代型の自律型リサーチエージェントです。
Slack上のチャットを通じて、AIが自律的にYouTube上の最新トレンドや競合動画を調査・分析し、レポーティングを行います。

---

## 🚀 サービス概要

従来のデータ収集ツールとは異なり、AI（Gemini）が「ユーザーの意図」を解釈し、必要に応じて自らYouTube APIを叩いて情報を取得します。

- **対話型リサーチ**: 「最近の〇〇業界の動向は？」と聞くだけで、AIが最新動画を検索し要約。
- **24時間常駐型**: Google Cloud Run（常時起動）により、スマホのSlackアプリからもいつでも利用可能。
- **高精度な分析**: 単なる検索結果の羅列ではなく、視聴者の反応やコメント傾向を考慮した分析結果を返信。

---

## 🛠 技術スタック

- **Backend**: Python 3.10+ / FastAPI
- **AI Brain**: Google Gemini 2.0 Flash / 1.5 Pro
- **API**: YouTube Data API v3 / Slack Bolt SDK
- **Infrastructure**: Google Cloud Run / Docker

---

## 📦 ファイル構成

- `main.py`: アプリケーション本体（FastAPI & AIロジック）
- `requirements.txt`: 依存ライブラリ一覧
- `Dockerfile`: コンテナ構築用設定
- `README.md`: 本ドキュメント

---

## ⚙️ セットアップ手順

### 1. APIキーの取得
以下のAPIキーを準備してください。
- **Slack**: Bot User OAuth Token (`xoxb-`), Signing Secret
- **Google AI Studio**: Gemini API Key
- **Google Cloud**: YouTube Data API v3 Key

### 2. Slack Appの設定
1. [Slack API](https://api.slack.com/apps) で「From scratch」からアプリを作成。
2. **OAuth & Permissions** で以下の Scopes を追加：
   - `app_mention:read`
   - `chat:write`
3. **Event Subscriptions** を有効にし、Cloud Runデプロイ後に発行されるURLを登録（後述）。

### 3. Google Cloud Run へのデプロイ
1. 本リポジトリをGitHubにプッシュ。
2. Google Cloud コンソールの **Cloud Run** から「サービスの作成」を選択。
3. 「リポジトリから継続的にデプロイする」を選択し、本リポジトリを連携。
4. **変数とシークレット** タブで、以下の環境変数を設定：
   - `SLACK_BOT_TOKEN`
   - `SLACK_SIGNING_SECRET`
   - `GEMINI_API_KEY`
   - `YOUTUBE_API_KEY`
5. 作成をクリックしてデプロイを完了させる。

### 4. Slackイベントの疎通確認
1. デプロイ完了後、発行されたURLに `/slack/events` を付けたものをSlack管理画面の **Request URL** に入力。
   - 例: `https://youtube-bot-xxxx.a.run.app/slack/events`
2. 「Verified」と表示されたら、`app_mention` イベントを購読。

---

## 💡 使い方例

SlackのチャンネルでBotにメンションを送って指示を出します。

> **ユーザー**: `@YouTube調査君 AIツールの最新トレンド動画を3つ探して、日本語で要約して。`
>
> **AI**: `YouTubeを調査中... 以下の3つの動画が現在注目されています。[動画1の要約]...`

---

## 👨‍💻 開発者情報
**萬俵 (Manpyo)**
- フリーランスエンジニア（2019年〜）
- 総受注174件 / 顧客満足度97%
- YouTube API / Google Maps APIを活用した業務自動化・AIエージェント構築を専門としています。

---

## ⚖️ ライセンス
MIT License
