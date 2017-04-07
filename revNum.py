from __future__ import print_function
test_cases = int(raw_input().strip())
for i in range(test_cases):
    num = int(raw_input().strip())
    while(num > 0):
        dig = num % 10
        if dig != 0:
            print(num % 10, end='')
        num /= 10
        num = int(num)
    print()
