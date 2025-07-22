from typing import Dict, List

import g4f
from g4f.client import Client
from zhipuai import ZhipuAI

g4f.debug.logging = True


def chat_completion(message: List[Dict], method: str = 'g4f', api_key: str = None, vlm: bool = False) -> str:
    """Use OpenAI API via gpt4free providers"""
    try:
        if method == 'g4f':
            client = Client()
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=message,
                ignored=["Cnote", "Aichatos"]
            )
            response = response.choices[0].message.content
        elif method == 'zhipuai':
            client = ZhipuAI(api_key=api_key)
            if not vlm:
                response = client.chat.completions.create(
                    model="glm-4-flash",
                    messages=message,
                )
            else:
                response = client.chat.completions.create(
                    model="glm-4v-flash",
                    messages=message
                )
            response = response.choices[0].message.content
        print(f"Successfully called {method} model.")
        return response

    except Exception as e:
        response = (
        "There're something wrong in openai api, please try again.\n"
        "Or connect to developer: https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues \n"
        f"{e}"
        )
        print(e)

    return response
