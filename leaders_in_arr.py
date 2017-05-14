test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    list_size = int(input().strip())
    num_arr = input().strip().split(' ')
    num_arr = [int(i) for i in num_arr]

    max_num = num_arr[-1]
    leaders = [max_num]
    # print(max_num, end=' ')

    for a_num in num_arr[-2::-1]:
        if max_num < a_num:
            max_num = a_num
            leaders.append(max_num)
            # print(max_num, end=' ')
    for a_num in leaders[::-1]:
        print(a_num, end=' ')
    print()
        
