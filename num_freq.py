test_cases = int(input().strip())

for a_tc in range(test_cases):
    list_len = int(input().strip())
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    freq_list = [0] * list_len

    for a_num in num_list:
        freq_list[a_num - 1] += 1

    for freq in freq_list:
        print(freq, end=' ')
    print()
