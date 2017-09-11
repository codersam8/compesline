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
        print(str(bi_tree_node.ele) + ' ', end=' ')

    
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

    def in_order_output(self):
        self.in_order(self.the_output)

    def the_in_order(self, btn):
        if btn:
            self.the_in_order(btn.lc)
            linked_binary_tree.visit(btn)
            self.the_in_order(btn.rc)

    def in_order(self, visit):
        linked_binary_tree.visit = visit
        self.the_in_order(self.root)

    def post_order_output(self):
        self.post_order(self.the_output)

    def the_post_order(self, btn):
        if btn:
            self.the_post_order(btn.lc)
            self.the_post_order(btn.rc)
            linked_binary_tree.visit(btn)

    def post_order(self, visit):
        linked_binary_tree.visit = visit
        self.the_post_order(self.root)


if __name__ == '__main__':
    a = linked_binary_tree()
    w = linked_binary_tree()
    x = linked_binary_tree()
    y = linked_binary_tree()
    z = linked_binary_tree()
    w.make_tree(1, a, a)
    x.make_tree(2, a, a)
    y.make_tree(3, w, x)
    z.make_tree(4, y, a)
    print("Preorder sequence is ")
    z.pre_order_output()
    print()

    print('Inorder sequence is ')
    z.in_order_output()
    print()

    print('Postorder sequence is ')
    z.post_order_output()
    print()
