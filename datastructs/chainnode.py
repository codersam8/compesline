class ChainNode:

    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    def __str__(self):
        return str(self.element)
