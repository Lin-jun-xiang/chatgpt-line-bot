from chatgpt_linebot.memory import Memory
from chatgpt_linebot.modules.gpt import chat_completion as chat


def chat_completion(id: int, memory: Memory) -> str:
    """Use OpenAI API via gpt4free providers"""
    response = chat(memory.get(id))
    memory.append(id, 'system', response)
    print(memory.storage)
    return response
