import json
import random

import g4f

from chatgpt_linebot.prompts import youtube_recommend_template

path = './data/favorite_videos.json'

with open(path, 'r', encoding='utf-8') as file:
    favorite_videos = json.load(file)


def recommend_videos():
    """Recommend youtube videos randomly"""
    push_video = random.sample(favorite_videos, 3)

    prompt = f"{youtube_recommend_template}{push_video}"

    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": prompt}],
        )
        return response
    except Exception as e:
        print(e)
