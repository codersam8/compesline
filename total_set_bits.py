# http://practice.geeksforgeeks.org/problems/count-total-set-bits/0
tc = int(input().strip())


def get_left_most_bit(a_num):
    l_most = 0

    while a_num > 1:
        l_most += 1
        a_num = a_num >> 1
    # print('l_most', l_most)
    return l_most


def count_set_bits2(a_num, l_most):
    if a_num == 0:
        return 0

    if a_num == (1 << (l_most + 1)) - 1:
        return ((l_most + 1) * (1 << l_most))

    a_num = a_num - (1 << l_most)
    # print('*' * 80)
    # print('a_num', a_num)

    return (a_num + 1) + count_set_bits(a_num) + l_most * (1 << (l_most - 1))


def count_set_bits(a_num):
    l_most = get_left_most_bit(a_num)
    return count_set_bits2(a_num, l_most)


for a_tc in range(tc):
    a_num = int(input().strip())
    # print('*' * 80)
    # print('a_num', a_num)

    print(count_set_bits(a_num))
