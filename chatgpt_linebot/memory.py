from typing import Dict
from collections import defaultdict


class MemoryInterface:
    def append(self, user_id: str, message: Dict) -> None:
        pass

    def get(self, user_id: str) -> str:
        return ""

    def remove(self, user_id: str) -> None:
        pass


class Memory(MemoryInterface):
    """Chat Memory
    
    Args:
        storage (List[Dict[str, str]]): Chat history, ex: 
        [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', content': 'Hi'},
            {'role': 'system', 'content': 'Hi. How can i assist u?'},
            ...
        ]

        id (int): user_id, grouop_id, room_id
    """
    def __init__(self, memory_message_count: int, system_prompt: str = '') -> None:
        self.storage = defaultdict(list)
        self.image_storage = {}
        self.memory_message_count = memory_message_count
        self.system_prompts = defaultdict(lambda: system_prompt)

    def _initialize(self, id: str) -> None:
        self.storage[id] = [{
            'role': 'system', 'content': self.system_prompts[id]
        }]

    def _drop_message(self, id: str) -> str:
        if len(self.storage.get(id)) >= (self.memory_message_count + 1) * 2 + 1:
            self.storage[id] = [self.storage[id][0]] + self.storage[id][-(self.memory_message_count * 2):]
        return self.storage.get(id)

    def append(self, id: str, role: str, content: str) -> None:
        if self.storage[id] == []:
            self._initialize(id)
        self.storage[id].append({
            'role': role,
            'content': content
        })
        self._drop_message(id)

    def get(self, id: str) -> str:
        if not self.storage[id]:
            self._initialize(id)
        return self.storage[id]

    def remove(self, id: str) -> None:
        self.storage[id] = []
        if id in self.system_prompts:
            del self.system_prompts[id]

    def set_system_prompt(self, id: str, prompt: str) -> None:
        self.system_prompts[id] = prompt
        self._initialize(id)
