# http://practice.geeksforgeeks.org/problems/reverse-sub-array/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    a_len = int(input().strip())
    a_list = input().strip()
    a_list = a_list.split(' ')
    a_list = [int(i) for i in a_list]
    s_e = input().strip().split()
    s_e = [int(i) for i in s_e]
    st, end = s_e[0] - 1, s_e[1] - 1
    print(st, end)
    while(st < end):
        temp = a_list[st]
        a_list[st] = a_list[end]
        a_list[end] = temp
        st += 1
        end -= 1

    for a_val in a_list:
        print(a_val, end=' ')
    print()
    
