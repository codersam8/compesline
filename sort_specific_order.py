# http://www.practice.geeksforgeeks.org/problem-page.php?pid=1696
from quick_sort import quick_sort

def separate_odd_even(num_arr):
    l = 0
    r = len(num_arr) - 1

    while(l < r):
        while((num_arr[l] % 2) != 0):
            l += 1
        while((num_arr[r] % 2) == 0):
            r -= 1
        if(l < r):
            num_arr[l], num_arr[r] = num_arr[r], num_arr[l]
        else:
            l -= 1
    print(l)
    print (num_arr)
    return l
test_cases = int(input().strip())

for a_tc in range(test_cases):
    input()
    num_arr = input().strip().split(' ')
    num_arr = [int(i) for i in num_arr]
    # print(num_arr)
    last_odd = separate_odd_even(num_arr)
    quick_sort(num_arr, last_odd + 1, len(num_arr) - 1)
    print(num_arr)
