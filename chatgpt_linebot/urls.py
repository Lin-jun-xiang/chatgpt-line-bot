import sys

import g4f
from fastapi import APIRouter, HTTPException, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from chatgpt_linebot.memory import Memory
from chatgpt_linebot.prompts import girlfriend

sys.path.append(".")

import config

line_app = APIRouter()
memory = Memory(3)

line_bot_api = LineBotApi(config.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(config.LINE_CHANNEL_SECRET)


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


def chat_completion(user_id: int) -> str:
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=memory.get(user_id),
        )
        memory.append(user_id, 'system', response)

    except Exception as e:
        response = (
        f"There're something wrong, please try again.\n"
        "Or connect to developer: https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues"
        )
        print(e)

    return response


@handler.add(MessageEvent, message=(TextMessage))
def handle_message(event) -> None:
    """Event - User sent message

    Args:
        event (LINE Event Object): Refer to https://developers.line.biz/en/reference/messaging-api/#message-event
    """
    reply_token = event.reply_token
    user_id = event.source.user_id

    # Text message
    if isinstance(event.message, TextMessage):
        # Get user sent message
        pre_prompt = girlfriend
        user_message = f"{pre_prompt}:\n{event.message.text}"
        memory.append(user_id, 'user', user_message)
        response = chat_completion(user_id)

        # Reply with same message
        messages = TextSendMessage(text=response)
        line_bot_api.reply_message(reply_token=reply_token, messages=messages)
