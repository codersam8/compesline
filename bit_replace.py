def change_10(bin_num):
    num = 0
    pow = 0
    for a_bin_num in bin_num[::-1]:
        num += int(a_bin_num) * (2 ** pow)
        pow += 1
    return num
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    num_pos = input().strip().split(' ')
    num_pos = [int(i) for i in num_pos]
    num, pos = num_pos[0], num_pos[1]
    bin_num = bin(num)
    bin_num = bin_num[2:]
    if bin_num[pos - 1] == '1':
        # print(bin_num)
        bin_num = list(bin_num)
        bin_num[pos - 1] = '0'
        # print(bin_num)
        flipped_num = change_10(bin_num)
        print(flipped_num)
    else:
        print(num)
