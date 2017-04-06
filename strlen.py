# http://practice.geeksforgeeks.org/problems/string-with-numbers-at-its-end/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    str_len = input().strip()
    total_len = len(str_len)
    # print(total_len)
    num = 0
    num_of_digits = 0
    pow_ten = 1
    for a_char in str_len[::-1]:
        if ord('0') <= ord(a_char) <= ord('9'):
            # didn't thougt of forming the number this way
            num += (int(a_char) * pow_ten)
            # the above method is different from regular way I used to do
            pow_ten *= 10
            # calculating digits hear itself
            num_of_digits += 1
        else:
            break
    # print(num_of_digits)
    # print(num)
    if (total_len - num_of_digits) == num:
        print(1)
    else:
        print(0)
