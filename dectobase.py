def divide(div, base):
    if div >= base:
        divide(int(div / base), base)
        rem = div % base
        # we are printing after method call
        # this is important for recursion
        if rem > 9:
            # I tried printing div which was wrong
            print(chr(ord('A') + rem - 10), end='')
        else:
            print(rem, end='')
    else:
        print (div, end='')

test_cases = int(input().strip())
# print("test cases " + str(test_cases))
for test_case in range(test_cases):
    base = int(input().strip())
    dec_num = int(input().strip())
    divide(dec_num, base)
    print()


