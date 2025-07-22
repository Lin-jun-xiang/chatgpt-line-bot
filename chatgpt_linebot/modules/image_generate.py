import re

import requests
from zhipuai import ZhipuAI


def generate_image(query: str, api_key: str) -> str:
    """Should setup the cookies first."""
    try:
        client = ZhipuAI(api_key=api_key)

        response = client.images.generations(
            model="cogview-3-flash",
            prompt=query,
        )
        image_url = response.data[0].url
        print(f'Successfully generated image from Zhipuai: {image_url}')
        return image_url

    except Exception as e:
        print(
        "There're something wrong in openai api, please try again.\n"
        "Or connect to developer: https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues \n"
        f"{e}"
        )


class RapidAPIs:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def ai_text_to_img(self, prompt: str) -> str:
        """https://rapidapi.com/bussinesonline250/api/ai-text-to-image-generator-api
        ```python
        prompt = '#c dogs' | '#r dogs' | '#3d dogs'
        ```
        """
        hash_style = {
            'c': 'cyberpunk',
            'r': 'realistic',
            '3d': '3D'
        }
        pattern = r'#([a-zA-Z0-9]+)'
        style = hash_style.get(re.search(pattern, prompt).group(1))

        url = f"https://ai-text-to-image-generator-api.p.rapidapi.com/{style}"

        payload = {"inputs": prompt}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "ai-text-to-image-generator-api.p.rapidapi.com"
        }
        response = requests.post(url, json=payload, headers=headers)
        print("Rapid API - AI Text to Image...")
        return response.json()['url']
