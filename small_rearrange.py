test_cases = int(input().strip())

for a_tc in range(test_cases):
    a_num_str = (input().strip())
    freq_list = [0] * 10
    idx = 0
    while a_num_str[idx] == '0':
        freq_list[0] += 1
        idx += 1
    a_num = int(a_num_str)

    while a_num:
        curr_dig = a_num % 10
        freq_list[curr_dig] += 1
        a_num //= 10
    # print('*' * 80)
    # print('freq_list', freq_list)

    result = 0

    for a_val in range(1, 10):
        # print('*' * 80)
        # print('a_val freq_list[a_val] result', a_val, freq_list[a_val], result)
        if freq_list[a_val]:
            result = a_val
            freq_list[a_val] -= 1
            break

    for idx in range(10):
        while freq_list[idx]:
            # print('*' * 80)
            result = (result * 10) + idx
            # print('result', result)
            freq_list[idx] -= 1
            # print('*' * 80)
            # print('freq_list', freq_list)

    print(result)
