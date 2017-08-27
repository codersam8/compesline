class EdgeNode:
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return str(self.v)

    def __eq__(self, other):
        return self.v == other.v
