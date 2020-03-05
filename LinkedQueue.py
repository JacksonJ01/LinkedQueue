from LinkedListTail import *


class Queue:
    def __init__(self):
        self.queue = LinkedListTail()

    def push(self, data):
        return self.queue.add_tail(data)

    def pop(self):
        return self.queue.remove_head()

    def peak(self):
        return self.queue.head.data
