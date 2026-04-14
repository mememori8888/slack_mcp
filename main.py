import os
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
import google.generativeai as genai

# --- 1. Slack App (Bolt) の設定 ---
# Signing Secretによる認証を自動で行います
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
handler = SlackRequestHandler(app)

# --- 2. Gemini & 萬俵ツールの設定 ---
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# 萬俵さんのYouTube APIロジック（ツール）を定義
def search_youtube_videos(keyword: str):
    """YouTubeで動画を検索し、タイトルとURLを返します。"""
    # ここに萬俵さんの既存のYouTube Data APIロジックを入れる
    print(f"DEBUG: YouTubeで '{keyword}' を検索中...")
    return [{"title": "最新AI解説動画", "url": "https://youtube.com/..."}]

# Geminiの設定（ツールを教える）
tools = [search_youtube_videos]
model = genai.GenerativeModel(model_name='gemini-1.5-flash', tools=tools)

# --- 3. Slack イベント処理 (メンション) ---
@app.event("app_mention")
def handle_mention(event, say):
    user_query = event['text']
    
    # Geminiに相談（自動関数呼び出しを有効化）
    chat = model.start_chat(enable_automatic_function_calling=True)
    response = chat.send_message(user_query)
    
    # Slackに返信
    say(f"<@{event['user']}> さん、調査結果です！\n{response.text}")

# --- 4. FastAPI の設定 ---
api_app = FastAPI()

@api_app.post("/slack/events")
async def slack_events(request: Request):
    # SlackからのリクエストをBoltのハンドラーに渡す
    return await handler.handle(request)

# ヘルスチェック用（Cloud Runが正常起動しているか確認するため）
@api_app.get("/")
async def root():
    return {"status": "ok"}
