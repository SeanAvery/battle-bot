from collections import deque
import random

class Memory():
    def __init__(self, max_size):
        self.memories = deque()
        self.max_size = max_size

    def append(self, item):
        if len(self.memories) > self.max_size - 1:
            self.memories.popleft()
            self.memories.append(item)
        else:
            self.memories.append(item)

        print('length of memeories', len(self.memories))
