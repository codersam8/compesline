test_cases = int(input().strip())


def compute_char_count(str_2):
    char_count_list = [True] * 256
    for a_char in str_2:
        char_count_list[ord(a_char)] = False
    return char_count_list


for a_tc in range(test_cases):
    str_1 = input().strip()
    str_2 = input().strip()

    char_count_list = compute_char_count(str_2)
    str_list = list(str_1)
    op_list = []
    for a_char in str_list:
        if char_count_list[ord(a_char)]:
            op_list.append(a_char)

    print(''.join(op_list))
