# queue 구현하기

class Queue:
    def __init__(self):
        self.queue = []

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.empty():
            return "비어있는 queue입니다."
        else:
            dequeued_data = self.queue[0]
            self.queue = self.queue[1:]
            return dequeued_data
