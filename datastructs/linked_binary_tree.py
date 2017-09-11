from binary_tree_node import BinaryTreeNode


class linked_binary_tree:
    visit = None
    def __init__(self):
        self.root = None

    def make_tree(self, root, left, right):
        self.root = BinaryTreeNode(root,
                                   left.root,
                                   right.root)

    def the_output(self, bi_tree_node):
        print(str(bi_tree_node.ele) + ' ')

    
    def pre_order_output(self):
        self.pre_order(self.the_output)

    def the_pre_order(self, btn):
        if btn:
            linked_binary_tree.visit(btn)
            self.the_pre_order(btn.lc)
            self.the_pre_order(btn.rc)

    def pre_order(self, visit):
        linked_binary_tree.visit = visit
        self.the_pre_order(self.root)


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
    z.pre_order_output()
    print()
