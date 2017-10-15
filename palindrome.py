# http://practice.geeksforgeeks.org/problems/palindrome-string/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    a_len = input()
    # print(a_len)
    a_str = input().strip()
    for idx in range(len(a_str) // 2):
        if a_str[idx] != a_str[-(idx + 1)]:
            print('No')
            break
    else:
        print('Yes')
