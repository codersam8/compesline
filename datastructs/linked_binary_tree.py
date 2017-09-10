from binary_tree_node import BinaryTreeNode


class linked_binary_tree:
    def __init__(self):
        self.root = None

    def make_tree(self, root, left, right):
        self.root = BinaryTreeNode(root,
                                   left.root,
                                   right.root)

    def the_output(bi_tree_node):
        print(bi_tree_node.ele + ' ')

    def pre_order_output():
        pre_order(the_output)


if __name__ == '__main__':
    a = linked_binary_tree()
    w = linked_binary_tree()
    x = linked_binary_tree()
    y = linked_binary_tree()
    z = linked_binary_tree()
    w.make_tree(1, a, a)
    x.make_tree(2, a, a)
    y.make_tree(3, w, x)
    z.make_tree(4, x, a)
    print("Preorder sequence is ")
