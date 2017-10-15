test_cases = int(input().strip())

for a_tc in range(test_cases):
    arr_len = int(input().strip())
    arr = input().strip().split()

    for idx in range(arr_len // 2):
        arr[idx], arr[-(idx + 1)] = arr[-(idx + 1)], arr[idx]

    for val in arr:
        print(val, end=' ')
    print()
