# from __future__ import print_function
test_cases = int(input().strip())
for i in range(test_cases):
    num = int(input().strip())
    num_s = input().strip().split(' ')
    num_s = [int(i) for i in num_s]
    larger = 0
    largest = 0
    for a_num in num_s:
        if a_num > largest:
            larger = largest
            largest = a_num
            continue
        elif a_num > larger:
            larger = a_num
    print (larger)
