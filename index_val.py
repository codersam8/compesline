# http://practice.geeksforgeeks.org/problems/value-equal-to-index-value/0
tc = int(input().strip())

for a_tc in range(tc):
    input()
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    # print(num_list)
    found = False
    for ind in range(len(num_list)):
        if (ind + 1) == num_list[ind]:
            print(ind + 1, end=' ')
            found = True
    if not found:
        print('Not Found', end='')
    print()
