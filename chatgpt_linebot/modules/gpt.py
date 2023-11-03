from typing import Dict, List

import g4f


def chat_completion(message: List[Dict]) -> str:
    """Use OpenAI API via gpt4free providers"""
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=message,
        )
        print(response)

    except Exception as e:
        response = (
        "There're something wrong in openai api, please try again.😱\n"
        "Or connect to developer: https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues"
        )
        print(e)

    return response
