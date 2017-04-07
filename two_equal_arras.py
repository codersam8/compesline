test_cases = int(input().strip())

for tc in range(test_cases):
    equal  = True
    input()
    arr1 = input().strip().split(' ')
    arr1 = [int(i) for i in arr1]

    arr2 = input().strip().split(' ')
    arr2 = [int(i) for i in arr2]

    num_count = {}

    for a_num in arr1:
        if a_num in num_count:
            num_count[a_num] += 1
        else:
            num_count[a_num] = 1

    for a_num in arr2:
        if a_num not in num_count:
            print(0)
            equal = False
            break
        if num_count[a_num] == 0:
            print(0)
            equal = False
            break
        num_count[a_num] -= 1
    if equal:
        print(1)
