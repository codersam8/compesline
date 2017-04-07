test_cases = int(input().strip())

for tc in range(test_cases):
    input()
    num_arr = input().strip().split(' ')
    num_arr = [int(i) for i in num_arr]
    num_count = {}

    for a_num in num_arr:
        if a_num in num_count:
            num_count[a_num] += 1
        else:
            num_count[a_num] = 1

    for k, v in num_count.items():
        if v == 1:
            print(k)
            break
