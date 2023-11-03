import json
import random

from chatgpt_linebot.modules.gpt import chat_completion
from chatgpt_linebot.prompts import youtube_recommend_template

path = './data/favorite_videos.json'

with open(path, 'r', encoding='utf-8') as file:
    favorite_videos = json.load(file)


def recommend_videos():
    """Recommend youtube videos randomly"""
    push_video = random.sample(favorite_videos, 3)

    prompt = f"{youtube_recommend_template}{push_video}"
    response = chat_completion([{"role": "user", "content": prompt}])

    return response
