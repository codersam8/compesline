# http://practice.geeksforgeeks.org/problems/armstrong-numbers/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    a_num = int(input().strip())
    a_num2 = a_num
    tot = 0
    while a_num > 0:
        dig = a_num % 10
        tot += dig ** 3
        a_num //= 10
    if tot == a_num2:
        print('Yes')
    else:
        print('No')
