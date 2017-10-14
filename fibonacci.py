test_cases = int(input().strip())
feb_list = [0, 1]


def find_nth_feb(nth):
    if nth < len(feb_list):
        return feb_list[nth]
    else:
        curr_len = len(feb_list)
        a = feb_list[curr_len - 2]
        b = feb_list[curr_len - 1]
        for val in range(curr_len, nth + 1):
            temp = a + b
            a = b
            b = temp
            feb_list.append(temp)
    return feb_list[nth]


for a_tc in range(test_cases):
    nth = int(input().strip())
    nth_num = find_nth_feb(nth)
    # print(feb_list)
    print(nth_num % 1000000007)
