# http://practice.geeksforgeeks.org/problems/binary-number-to-decimal-number/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    a_bin = input().strip()
    dec = 0
    a_pow = 0
    for dig in a_bin[::-1]:
        dec += (int(dig) * (2 ** a_pow))
        a_pow += 1
    print(dec)
