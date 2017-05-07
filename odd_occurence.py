# http://practice.geeksforgeeks.org/problems/find-the-odd-occurence/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    arr_len = int(input().strip())
    num_arr = input().strip().split(' ')
    num_arr = [int(i) for i in num_arr]

    odd_occ = 0
    for a_num in num_arr:
        odd_occ = odd_occ ^ a_num
    print(odd_occ)
