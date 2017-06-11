ugly_numbers = [1]

def ugly_num_generator():
    i2 = [1]
    i3 = [1]
    i5 = [1]
    next_multiple_of_2 = [2]
    next_multiple_of_3 = [3]
    next_multiple_of_5 = [5]

    def find_next_ugly_num(n):
        len_of_ugly_nums = len(ugly_numbers)
        while n > len_of_ugly_nums:
            next_ugly_num = min(next_multiple_of_2[0],
                                next_multiple_of_3[0],
                                next_multiple_of_5[0])
            ugly_numbers.append(next_ugly_num)
            len_of_ugly_nums += 1
            # using only ifs here for a reason
            if next_ugly_num == next_multiple_of_2[0]:
                next_multiple_of_2[0] = 2 * ugly_numbers[i2[0]]
                i2[0] += 1
            if next_ugly_num == next_multiple_of_3[0]:
                next_multiple_of_3[0] = 3 * ugly_numbers[i3[0]]
                i3[0] += 1
            if next_ugly_num == next_multiple_of_5[0]:
                next_multiple_of_5[0] = 5 * ugly_numbers[i5[0]]
                i5[0] += 1
        return ugly_numbers[n - 1]
    return find_next_ugly_num

find_next_ugly_num = ugly_num_generator()

test_cases = int(input())

for a_tc in range(test_cases):
    n_val = int(input())
    nth_ugly_num = find_next_ugly_num(n_val)
    print(nth_ugly_num)

