http://www.practice.geeksforgeeks.org/problem-page.php?pid=1687
test_cases = int(input().strip())

def check_for_asc(num_arr, start):
    asc = False
    # for single anti-clockwise
    trk = start
    for trk in range(start, arr_len - 1):
            # checking for ascending
        if num_arr[trk] < num_arr[trk + 1] :
            if trk == arr_len - 2:
                asc = True
        else:
            break
        # not comparing trk value because single clockwise
    if start > arr_len - 2:
        asc = True
    return asc, trk

def check_for_des(num_arr, start):
    dec = False
    trk = start
    for trk in range(start, arr_len - 1):
        # checking for decending
        if num_arr[trk] > num_arr[trk + 1] :
            if trk == arr_len - 2:
                dec = True
        else:
            break
    if start > arr_len - 2:
        dec = True
    return dec, trk

for a_tc in range(test_cases):
    arr_len = int(input())

    num_arr = input().strip().split(' ')
    num_arr = [int(i) for i in num_arr]
    rotated, trk = check_for_asc(num_arr, 0)
    # looking for ascending
    if rotated:
        print(num_arr[(trk + 1)], end=' ')
        print(1)
    # for ascending rotated
    elif not rotated:
        rotated = check_for_asc(num_arr, trk + 1)[0]

        if rotated:
            print(num_arr[(trk)], end=' ')
            print(4)
        # for descending
        elif not rotated:
            rotated, trk = check_for_des(num_arr, 0)

            if rotated:
                print(num_arr[0], end=' ')
                print(2)
                # for descending rotated
            else:
                rotated = check_for_des(num_arr, trk + 1)[0]
                if rotated:
                    print(num_arr[trk + 1], end=' ')
                    print(3)
            
        
