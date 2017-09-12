# http://practice.geeksforgeeks.org/problems/maximum-product-of-two-numbers/0
tc = int(input().strip())

for a_tc in range(tc):
    input()
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    maxer = maxest = 0
    for val in num_list:
        # print(val, end=' ')
        if val > maxest:
            maxer = maxest
            maxest = val
        elif val > maxer:
            maxer = val
        # print(maxer, maxest)
    print(maxer * maxest)
