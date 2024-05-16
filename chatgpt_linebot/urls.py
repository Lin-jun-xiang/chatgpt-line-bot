import sys

from fastapi import APIRouter, HTTPException, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from chatgpt_linebot.memory import Memory
from chatgpt_linebot.modules import (
    Horoscope,
    ImageCrawler,
    RapidAPIs,
    chat_completion,
    g4f_generate_image,
    recommend_videos,
)
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


def handle_image_search(reply_token, query):
    """Handles image search requests."""
    try:
        img_url = search_image_url(query)
        if img_url:
            send_image_reply(reply_token, img_url)
        else:
            send_text_reply(reply_token, 'Image cannot search successfully.')
    except Exception as e:
        send_text_reply(reply_token, f'Image search failed.\n{e}')


def handle_image_generation(reply_token, text, generator):
    """Handles requests to generate images using different APIs."""
    try:
        img_url = generate_image_url(text, generator)
        if img_url:
            send_image_reply(reply_token, img_url)
        else:
            send_text_reply(reply_token, 'Image cannot generate successfully.')
    except Exception as e:
        send_text_reply(reply_token, f'Image generation failed.\n{e}')


def handle_text_reply(event, user_message, reply_token):
    """Handles text messages and commands."""
    response = None

    if user_message.startswith('@chat 星座運勢'):
        response = horoscope.get_horoscope_response(user_message)
    else:
        response = handle_chat(event, user_message)

    if response:
        send_text_reply(reply_token, response)


def handle_chat(event, user_message):
    """Handles chat operations and memory interactions."""
    source_type = event.source.type
    print(source_type)
    source_id = getattr(event.source, f"{source_type}_id", None)

    if source_type == 'user':
        user_name = line_bot_api.get_profile(source_id).display_name
        print(f'{user_name}: {user_message}')
        memory.append(source_id, 'user', f"{girlfriend}:\n {user_message}")
        return chat_completion(source_id, memory)

    elif source_type in ['group', 'room']:
        if user_message.startswith('@chat'):
            memory.append(source_id, 'user', f"{girlfriend}:\n {user_message.replace('@chat', '')}")
            return chat_completion(source_id, memory)


def search_image_url(query):
    """Fetches image URL from different search sources."""
    img_crawler = ImageCrawler(nums=5)
    img_url = img_crawler.get_url(query)
    if not img_url:
        img_serp = ImageCrawler(engine='serpapi', nums=5, api_key=config.SERPAPI_API_KEY)
        img_url = img_serp.get_url(query)
        print('Used Serpapi search image instead of icrawler.')
    return img_url


def generate_image_url(text, generator) -> str:
    """Generates image URL using specified generator."""
    if generator == 'g4f':
        return g4f_generate_image(text)
    elif generator == 'rapid':
        return RapidAPIs(config.RAPID).ai_text_to_img(text)


def send_image_reply(reply_token, img_url):
    """Sends an image message to the user."""
    image_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
    line_bot_api.reply_message(reply_token, messages=image_message)


def send_text_reply(reply_token, text):
    """Sends a text message to the user."""
    text_message = TextSendMessage(text=text)
    line_bot_api.reply_message(reply_token, messages=text_message)


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
    user_message = event.message.text

    if user_message.startswith('@img'):
        handle_image_search(reply_token, user_message.replace('@img', ''))
    elif user_message.startswith('@ai_img_g4f'):
        handle_image_generation(reply_token, user_message.replace('@ai_img_g4f', ''), generator='g4f')
    elif user_message.startswith('@ai_img_rapid'):
        handle_image_generation(reply_token, user_message.replace('@ai_img_rapid', ''), generator='rapid')
    else:
        handle_text_reply(event, user_message, reply_token)


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

    if videos and "There're something wrong in openai api when call, please try again." not in videos:
        line_bot_api.broadcast(TextSendMessage(text=videos))

        # Push message to group via known group (event.source.group_id)
        known_group_ids = [
            'C6d-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Ccc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'Cbb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        ]
        for group_id in known_group_ids:
            line_bot_api.push_message(group_id, TextSendMessage(text=videos))

        print('Successfully recommended videos')
        return {"status": "success", "message": "recommended videos."}

    else:
        print('Failed recommended videos')
        return {"status": "failed", "message": "no get recommended videos."}