from collections import deque
import random

class Memory():
    def __init__(self, max_size):
        self.memories = deque()
        self.max_size = max_size

    def append(self, item):
        if len(self.memories) > self.max_size:
            self.memories.popleft()
            self.memories.append()
        else:
            self.memories.append(item)
