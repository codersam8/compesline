test_cases = int(input().strip())

def find_first(num_arr, low, hi, num_to_find):
    if low <= hi:
        mid = int((low + hi) / 2)

        if mid == 0 or num_to_find > num_arr[mid - 1] and num_to_find == num_arr[mid]:
            return mid
        elif num_to_find > num_arr[mid]:
            return find_first(num_arr, mid + 1, hi, num_to_find)
        else:
            return find_first(num_arr, low, mid - 1, num_to_find)

def find_last(num_arr, low, hi, num_to_find):
    if low <= hi:
        mid = int((low + hi) / 2)

        if mid < (len(num_arr)):
            if num_to_find < num_arr[mid + 1] and num_to_find == num_arr[mid]:
                return mid
        elif num_to_find < num_arr[mid]:
            return find_last(num_arr, low, mid - 1, num_to_find)
        else:
            return find_last(num_arr, mid + 1, hi, num_to_find)
    
for a_tc in range(test_cases):
    
    len_of_arr = int(input().strip())
    num_arr = input().strip().split(' ')
    num_to_find = int(input().strip())
    num_arr = [int(i) for i in num_arr]
    first = find_first(num_arr, 0, len_of_arr - 1, num_to_find)
    if first:
        print(first, end=' ')
    else:
        print(-1, end=' ')
    last = find_last(num_arr, 0 , len_of_arr - 1, num_to_find)
    if last:
        print(last)
    else:
        print(-1)

