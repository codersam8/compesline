# http://practice.geeksforgeeks.org/problems/possible-groups/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    arr_len = int(input().strip())
    arr = input().strip().split(' ')
    # print('*' * 80)
    # print('arr', arr)
    
    arr = [int(i) for i in arr]
    # amazing use of list in place of dict here 
    rem_arr = [0, 0, 0]
    tot_grps = 0
    # this loop is also amazing
    for a_num in arr:
        rem_arr[int(a_num % 3)] += 1

        # size 2 rem 0
    tot_grps = int(rem_arr[0] * (rem_arr[0] - 1) / 2)
    # size 2 with rem 1 and rem 2
    tot_grps += rem_arr[1] * rem_arr[2]
    # size 3 with all 0 rems
    tot_grps += int(rem_arr[0] * (rem_arr[0] - 1) * (rem_arr[0] - 2) / 6)
    # size 3 with all 1 rems
    tot_grps += int(rem_arr[1] * (rem_arr[1] - 1) * (rem_arr[1] - 2) / 6)
    # size 3 with all 2 rems
    tot_grps += int(rem_arr[2] * (rem_arr[2] - 1) * (rem_arr[2] - 2) / 6)
    # size 3 with different rems
    tot_grps += rem_arr[0] * rem_arr[1] * rem_arr[2]

    print(tot_grps)
    

    # print('*' * 80)
    # print('rem_arr', rem_arr)
    
        
