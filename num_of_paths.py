# http://practice.geeksforgeeks.org/problems/number-of-paths/0
tc = int(input().strip())


def count_paths(r, c):
    if r == 1 or c == 1:
        return 1
    return count_paths(r - 1, c) + count_paths(r, c - 1)


for a_tc in range(tc):
    r_c = input().strip().split()
    r_c = [int(i) for i in r_c]
    print(count_paths(*r_c))
