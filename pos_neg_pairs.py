test_cases = int(input().strip())

for a_tc in range(test_cases):
    input()
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    val_dict = {}

    for num in num_list:
        if abs(num) in val_dict:
            val_dict[abs(num)] += 1
        else:
            val_dict[abs(num)] = 1
    pairs_list = []
    for k, v in val_dict.items():
        if v == 2:
            pairs_list.append(k)

    pairs_list.sort()

    if pairs_list:
        for val in pairs_list:
            print(-val, val, end=' ')
    else:
        print(0, end=' ')
    print()
