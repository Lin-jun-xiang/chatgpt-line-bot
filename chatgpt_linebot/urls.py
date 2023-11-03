import sys

from fastapi import APIRouter, HTTPException, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from chatgpt_linebot.memory import Memory
from chatgpt_linebot.modules import Horoscope, chat_completion, recommend_videos
from chatgpt_linebot.prompts import girlfriend

sys.path.append(".")

import config

line_app = APIRouter()
memory = Memory(3)
horoscope = Horoscope()

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


@handler.add(MessageEvent, message=(TextMessage))
def handle_message(event) -> None:
    """Event - User sent message

    Args:
        event (LINE Event Object)

    Refs:
        https://developers.line.biz/en/reference/messaging-api/#message-event
        https://www.21cs.tw/Nurse/showLiangArticle.xhtml?liangArticleId=503
    """
    if not isinstance(event.message, TextMessage):
        return

    reply_token = event.reply_token
    user_id = event.source.user_id
    response = None

    # Get user sent message
    user_message = event.message.text
    pre_prompt = girlfriend
    refine_message = f"{pre_prompt}:\n{user_message}"

    if user_message.startswith('@chat 星座運勢'):
        response = horoscope.get_horoscope_response(user_message)

    elif event.source.type == 'user':
        memory.append(user_id, 'user', refine_message)
        response = chat_completion(user_id, memory)

    elif event.source.type == 'group' and user_message.startswith('@chat'):
        group_id = event.source.group_id
        memory.append(group_id, 'user', refine_message.replace('@chat', ''))
        response = chat_completion(group_id, memory)

    elif event.source.type == 'room' and user_message.startswith('@chat'):
        room_id = event.source.room_id
        memory.append(room_id, 'user', refine_message.replace('@chat', ''))
        response = chat_completion(room_id, memory)

    # Reply with same message
    if response:
        messages = TextSendMessage(text=response)
        line_bot_api.reply_message(reply_token=reply_token, messages=messages)


@line_app.get("/recommend")
def recommend_from_yt() -> None:
    """Line Bot Broadcast

    Descriptions
    ------------
    Recommend youtube videos to all followed users.
    (Use cron-job.org to call this api)

    References
    ----------
    https://www.cnblogs.com/pungchur/p/14385539.html
    https://steam.oxxostudio.tw/category/python/example/line-push-message.html
    """
    videos = recommend_videos()

    if videos:
        line_bot_api.broadcast(TextSendMessage(text=videos))
        
        # Push message to group via known group (event.source.group_id)
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))

    return {"status": "success", "message": "recommended videos."}
