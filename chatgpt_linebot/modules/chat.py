from chatgpt_linebot.memory import Memory
from chatgpt_linebot.modules.gpt import chat_completion as chat


def chat_completion(
    id: int,
    memory: Memory,
    method: str = 'g4f',
    api_key: str = None,
    vlm: bool = False,
) -> str:
    """Use OpenAI API via gpt4free providers"""
    response = chat(memory.get(id), method, api_key, vlm)
    print(memory.storage)
    return response
