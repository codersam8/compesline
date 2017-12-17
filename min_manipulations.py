test_cases = int(input().strip())

for a_tc in range(test_cases):
    str_len = int(input().strip())
    str1, str2 = input().strip().split()

    char_count = [0] * 26

    for char1 in str1:
        char_count[ord(char1) - ord('a')] += 1

    count = 0
    for char1 in str2:
        char_count[ord(char1) - ord('a')] -= 1
        if char_count[ord(char1) - ord('a')] < 0:
            count += 1
        # print(char_count)

    print(count)
