# implements linked linear list

from chainnode import ChainNode


class Chain:

    def __init__(self):
        self.size = 0
        self.first_node = None

    def __str__(self):
        chain_str = '['
        curr_node = self.first_node
        # modified because a chain can be empty
        while curr_node:
            chain_str += str(curr_node.element) + ', '
            curr_node = curr_node.next

        if self.size:
            chain_str = chain_str[:-2]
        chain_str = chain_str + ']'
        return chain_str

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get(self, idx):
        curr_node = self.first_node

        for i in range(idx):
            curr_node = curr_node.next

        return curr_node.element

    # TODO: implement index_of

    def index_of(self, ele):
        curr_node = self.first_node
        idx = 0
        while curr_node and curr_node.element != ele:
            curr_node = curr_node.next
            idx += 1
        if curr_node:
            return idx
        else:
            return -1

    def remove(self, idx):
        removed_element = None

        if idx == 0:
            removed_element = self.first_node.element
            first_node = self.first_node.next
        else:
            curr_node = first_node
            for i in range(idx - 1):
                curr_node = curr_node.next
            removed_element = curr_node.next.element
            curr_node.next = curr_node.next.next
        self.size -= 1
        return removed_element

    def add(self, idx, ele):
        if idx == 0:
            self.first_node = ChainNode(ele, self.first_node)
        else:
            curr_node = self.first_node
            for i in range(idx - 1):
                curr_node = curr_node.next

            curr_node.next = ChainNode(ele, curr_node.next)

        self.size += 1
