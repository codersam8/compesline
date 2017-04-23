# http://practice.geeksforgeeks.org/problems/total-count/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    l_t = (input().strip().split(' '))
    l_t = [int(i) for i in l_t]
    len_of_arr, tresh = l_t[0], l_t[1]

    in_arr = input().strip().split(' ')
    in_arr = [int(i) for i in in_arr]

    total_count = 0
    for a_num in in_arr:
        total_count += int(a_num / tresh)

        if not a_num % tresh == 0:
            total_count += 1

    print(total_count)
