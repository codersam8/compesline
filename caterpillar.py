# https://practice.geeksforgeeks.org/problems/jumping-caterpillars/0
tc = int(input().strip())

for a_t in range(tc):
    l_c = input().strip().split()
    l_c = [int(i) for i in l_c]
    # print(l_c)
    leaves = [1] * l_c[0]
    # print('leaves', leaves)
    cats = l_c[1]
    jumps = input().strip().split()
    jumps = [int(i) for i in jumps]
    # print('jumps', jumps)

    for a_cat in range(cats):
        jump_size = jumps[a_cat]
        # print('jump_size', jump_size)
        late_jump = jump_size
        # print('leaves', leaves)
        # print('late_jump', late_jump)
        while late_jump <= len(leaves):
            leaves[late_jump - 1] = 0
            late_jump += jump_size

    final_leaves = 0
    for a_leaf in leaves:
        if a_leaf:
            final_leaves += 1
    print(final_leaves)
