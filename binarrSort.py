# from __future__ import print_function
test_cases = int(input().strip())
for i in range(test_cases):
    bin_arr_len = int(input())
    bin_arr = input().strip().split(' ')
    zeroes = 0
    for a_bin in bin_arr:
        if a_bin == '0':
            zeroes += 1
    for a_trk in range(zeroes):
        print('0 ', end='')
    ones = bin_arr_len - zeroes
    for a_trk in range(bin_arr_len - zeroes - 1):
        print('1 ', end='')
    if ones:
        print('1')
        
