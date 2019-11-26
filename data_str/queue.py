

class queue:
    def __init__(self):
        self.queue_list = []
        self.index = 0

    def push(self, v):
        self.queue_list.append(v)

    def pop(self):
        element = self.queue_list[self.index]
        self.index += 1
        return element
