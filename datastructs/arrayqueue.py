class ArrayQueue:
    def __init__(self, init_cap=10):
        self.que = [None] * init_cap
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def put(self, ele):
        if (self.rear + 1) % len(self.que) == self.front:
            pass
        self.rear = (self.rear + 1) % len(self.que)
        self.que[self.rear] = ele

    def remove(self):
        if self.is_empty:
            return None
        self.front = (self.front + 1) % len(self.que)
        front_ele = self.que[self.front]
        self.que[self.front] = None
        return front_ele


aq = ArrayQueue(3)
