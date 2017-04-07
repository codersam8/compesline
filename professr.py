# from __future__ import print_function
test_cases = int(input().strip())
for i in range(test_cases):
    ppl = int(input().strip())
    col_list = input().strip().split(' ')
    col_list = [int(i) for i in col_list]
    min_col = min(col_list)
    max_col = max(col_list)
    # print(min_col, max_col)
    c_arr_size = max_col - min_col + 1
    # print(c_arr_size)
    c_arr = [0] * c_arr_size
    for colr in col_list:
        c_arr[colr - min_col] += 1
        if c_arr[colr - min_col] > 1:
            print('BOYS')
            break
    else:
         print('GIRLS') 
