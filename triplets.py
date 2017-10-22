test_cases = int(input().strip())

for a_tc in range(test_cases):
    list_size = int(input().strip())
    num_list = [int(i) for i in input().strip().split()]
    num_list.sort()
    count = 0
    found = False
    for idx in range(list_size-1, -1, -1):
        j = idx - 1
        k = 0

        while k < j:
            # print(num_list[idx], num_list[j], num_list[k])
            sum_val = (num_list[j] + num_list[k])
            if num_list[idx] == sum_val:
                count += 1
                # print('*' * 80)
                # print('count', count)
                found = True
                # break
                j -= 1
                k += 1
            elif num_list[idx] < sum_val:
                j -= 1
            else:
                k += 1
    if found:
        print(count)
    else:
        print(-1)
