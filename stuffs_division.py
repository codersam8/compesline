test_cases = int(input().strip())

for tc in range(test_cases):
    len_of_arr = int(input().strip())
    stuffs = input().strip().split(' ')
    stuffs = [int(i) for i in stuffs]
    arr_total = 0

    for a_stuff in stuffs:
        arr_total += a_stuff

    # print(arr_total)
    needed = len_of_arr * (len_of_arr + 1) / 2

    if arr_total == needed:
        print("YES")

    else:
        print("NO")
