def print_n(curr_num):
    if curr_num == 0:
        return
    print_n(curr_num - 1)
    print (curr_num, end=' ')
    
test_cases = int(input().strip())
for a_tc in range(test_cases):
    a_num = int(input().strip())
    print_n(a_num)
    print()
