def calc_sum(array_vals):
    sum_i = 0
    for i in array_vals:
        sum_i += i
    return sum_i

test_cases = int(input().strip())
# print("test_cases " + str(test_cases))
for i in range(test_cases):
    array_size = int(input().strip())
    # print("array_size " + str(array_size))
    array_vals = input().strip().split(' ')
    # print("array ")
    # print(array_vals)
    array_vals = [int(i) for i in array_vals]
    # print(array_vals)
    all_sum = int(array_size * (array_size + 1) / 2)
    arr_sum = calc_sum(array_vals)
    # print("missing number")
    print(all_sum - arr_sum)
