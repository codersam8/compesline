# http://practice.geeksforgeeks.org/problems/power-of-2/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    a_num = int(input().strip())
    a_num = 1 if not a_num else (a_num & (a_num - 1))
    if not a_num:
        print('YES')
    else:
        print('NO')
