# http://practice.geeksforgeeks.org/problems/sum-of-digits-divisibility/0

test_cases = int(input().strip())

for a_tc in range(test_cases):
    numbr = int(input().strip())
    sum_of_digs = 0
    numbr_cpy = numbr

    while numbr_cpy > 0:
        sum_of_digs += int(numbr_cpy % 10)
        numbr_cpy /= 10
    # print('*' * 80)
    # print('sum_of_digs', sum_of_digs)
    if int(numbr % sum_of_digs == 0):
        print(1)
    else:
        print(0)
    
    
