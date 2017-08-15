class Chain:

    def __init__(self):
        size = 0

    def is_empty():
        return size == 0

    def get_size():
        return size

    def get(idx):
        curr_node = first_node

        for i in range(idx):
            curr_node = curr_node.next

        return curr_node.element

    # TODO: implement index_of

    def remove(idx):
        removed_element = None

        if idx == 0:
            removed_element = first_node.element
            first_node = first_node.next
        else:
            curr_node = first_node
            for i in range(idx - 1):
                curr_node = curr_node.next
            removed_element = curr_node.next.element
            curr_node.next = curr_node.next.next
        size -= 1
        return removed_element

    def add(idx, ele):
        if idx == 0:
            first_node = ChainNode(ele, first_node)
        else:
            curr_node = first_node
            for i in range(idx - 1):
                curr_node = curr_node.next

            curr_node.next = ChainNode(ele, curr_node.next)

        size += 1
