# http://practice.geeksforgeeks.org/problems/count-zero/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    digs = int(input().strip())
    tot_num = 0
    for a_dig in range(2, digs + 1):
        curr_tot = (9 * ((10 ** (a_dig - 1)) - (9 ** (a_dig - 1))))
        tot_num += (9 * ((10 ** (a_dig - 1)) - (9 ** (a_dig - 1))))
    print(tot_num)
