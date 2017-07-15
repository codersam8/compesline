# http://practice.geeksforgeeks.org/problems/four-elements/0

test_cases = int(input().strip())

for a_tc in range(test_cases):
    len_a = int(input().strip())
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    tot = int(input().strip())
    found = False
    for i in range(len_a - 3):
        if found:
            break
        for j in range(i + 1, len_a - 2):
            if found:
                break
            for k in range(j + 1, len_a - 1):
                if found:
                    break
                for l in range(k + 1, len_a):
                    if (num_list[i] + num_list[j] +
                        num_list[k] + num_list[l] == tot):
                        found = True
                        break
    if found:
        print(1)
    else:
        print(0)
