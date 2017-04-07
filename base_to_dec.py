import numbers
test_cases = int(input().strip())
# print("test cases " + str(test_cases))
for test_case in range(test_cases):
    base = int(input().strip())
    base_num = (input().strip())[::-1]
    dec_num = 0
    curr_pow = 1
    for a_num in base_num:
        try:
            a_num = int(a_num)
            dec_num += a_num * curr_pow
        except Exception as e:
            # print(e)
            dec_num += (((ord(a_num) - ord('A')) + 10) * curr_pow)
        curr_pow *= base
    print( dec_num)


