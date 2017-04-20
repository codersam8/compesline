test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    a_num = int(input().strip())
    bits_set = 0
    while a_num > 0:
        a_num = a_num & (a_num - 1)
        bits_set += 1

    print(bits_set)
