# http://practice.geeksforgeeks.org/problems/number-of-occurrence/0
test_cases = int(input().strip())

def first(ip_arr, el, strt, end):
    # print('*' * 80)
    # print('start end', strt, end)
    
    if strt <= end:
        mid = int((strt + end) / 2)

        if mid == 0:
            if ip_arr[mid] == el:
                return mid
            else:
                return -1
        elif ip_arr[mid - 1] < el and ip_arr[mid] == el:
            return mid
        elif el <= ip_arr[mid]:
            return first(ip_arr, el, strt, mid - 1)
        else:
            return first(ip_arr, el, mid + 1, end)
    return -1

def last(ip_arr, el, strt, end):
    if strt <= end:
        mid = int((strt + end) / 2)

        if mid == len(ip_arr) - 1:
            if ip_arr[mid] == el:
                return mid
            else:
                return -1
        elif ip_arr[mid + 1] > el and ip_arr[mid] == el:
            return mid
        elif el >= ip_arr[mid]:
            return last(ip_arr, el, mid + 1, end)
        else:
            return last(ip_arr, el, strt, mid - 1)
    return -1


    
for a_tc in range(test_cases):
    
    siz_el = input().strip().split(' ')
    siz_el = [int(i) for i in siz_el]

    ip_arr = input().strip().split(' ')
    ip_arr = [int(i) for i in ip_arr]

    first_ind = first(ip_arr, siz_el[1], 0, siz_el[0] - 1)
    # print('*' * 80)
    # print('first_ind', first_ind)
    if first_ind != -1:
        last_ind = last(ip_arr, siz_el[1], 0, siz_el[0] - 1)
        print(last_ind - first_ind + 1)
    else:
        print(-1)
    
    
