# http://www.practice.geeksforgeeks.org/problem-page.php?pid=1696
# from quick_sort import quick_sort
# from quick_sort_dec import quick_sort_dec
def separate_odd_even(num_arr):
    left = 0
    r = len(num_arr) - 1

    while(left < r):
        while((num_arr[left] % 2) != 0 and left < r):
            left += 1
        while(((num_arr[r] % 2) == 0) and r > left):
            r -= 1
        if(left < r):
            num_arr[left], num_arr[r] = num_arr[r], num_arr[left]
        else:
            left -= 1
            return left
    # print(l)
    # print (num_arr)
    # return left
test_cases = int(input().strip())

for a_tc in range(test_cases):
    input()
    num_arr = input().strip().split(' ')
    num_arr = [int(i) for i in num_arr]
    # print(num_arr)
    last_odd = separate_odd_even(num_arr)
    num_arr[0: last_odd + 1] = sorted(num_arr[0: last_odd + 1], key=lambda odd_num: -odd_num)
    num_arr[last_odd+1: len(num_arr)] = sorted(num_arr[last_odd+1: len(num_arr)])
    # quick_sort_dec(num_arr, 0, last_odd)
    # quick_sort(num_arr, last_odd + 1, len(num_arr) - 1)
    for a_num in num_arr:
        print(a_num, end=' ')
    print()
