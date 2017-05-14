# http://practice.geeksforgeeks.org/problems/minimum-difference-pair/0

test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    arr_len = int(input().strip())
    num_arr = input().strip().split(' ')
    num_arr = [int(i) for i in num_arr]
    num_arr.sort()
    min_diff = num_arr[-1]
    for trk in range(arr_len - 1):
        curr_diff = abs(num_arr[trk] - num_arr[trk + 1])
        if min_diff > curr_diff:
            min_diff = curr_diff
    print(min_diff)
