test_cases = int(input().strip())

for tc in range(test_cases):
    len_of_arr = int(input().strip())
    arr1 = input().strip().split(' ')
    arr1 = [int(i) for i in arr1]

    num_count = {}

    for a_num in arr1:
        if a_num in num_count:
            num_count[a_num] += 1
        else:
            num_count[a_num] = 1

    for a_num in range(len_of_arr + 1):
        if (a_num) not in num_count:
            print(a_num, end=' ')
    print()
