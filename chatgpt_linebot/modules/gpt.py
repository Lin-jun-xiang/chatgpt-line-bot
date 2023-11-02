import g4f
from chatgpt_linebot.memory import Memory


def chat_completion(id: int, memory: Memory) -> str:
    """Use OpenAI API via gpt4free providers"""
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=memory.get(id),
        )
        memory.append(id, 'system', response)
        print(response)

    except Exception as e:
        response = (
        "There're something wrong in openai api, please try again.😱\n"
        "Or connect to developer: https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues"
        )
        print(e)

    return response
