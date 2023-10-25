import sys

import g4f
from fastapi import APIRouter, HTTPException, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

sys.path.append(".")

import config

line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)

line_app = APIRouter()


@line_app.post("/callback")
async def callback(request: Request) -> str:
    """LINE Bot webhook callback

    Args:
        request (Request): Request Object.

    Raises:
        HTTPException: Invalid Signature Error

    Returns:
        str: OK
    """
    signature = request.headers["X-Line-Signature"]
    body = await request.body()
    
    # handle webhook body
    try:
        handler.handle(body.decode(), signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Missing Parameter")
    return "OK"


@handler.add(MessageEvent, message=(TextMessage))
def handle_message(event) -> None:
    """Event - User sent message

    Args:
        event (LINE Event Object): Refer to https://developers.line.biz/en/reference/messaging-api/#message-event
    """
    reply_token = event.reply_token

    # Text message
    if isinstance(event.message, TextMessage):
        # Get user sent message
        user_message = event.message.text

        try:
          response = g4f.ChatCompletion.create(
              model=g4f.models.default,
              messages=[{"role": "user", "content": user_message}],
          )
        except Exception as e:
          response = f"Their're something wrong: {e}"

        # Reply with same message
        messages = TextSendMessage(text=response)
        line_bot_api.reply_message(reply_token=reply_token, messages=messages)
