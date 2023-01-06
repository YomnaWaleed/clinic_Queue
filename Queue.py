class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.insert(0, item)

    def dequeue(self):
        return self.elements.pop()

    def isEmpty(self):
        return self.elements == []

    def Size(self):
        return len(self.elements)

