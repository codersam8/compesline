# http://practice.geeksforgeeks.org/problems/check-set-bits/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    a_num = int(input().strip())
    if (a_num & (a_num + 1)) == 0:
        print('YES')
    else:
        print('NO')
