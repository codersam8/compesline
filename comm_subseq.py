test_cases = int(input().strip())

for a_tc in range(test_cases):
    str1, str2 = input().strip().split()
    str1_chars = [0] * 52
    str2_chars = [0] * 52

    for a_char in str1:
        str1_chars[ord(a_char) - ord('A')] = 1

    for a_char in str2:
        str2_chars[ord(a_char) - ord('A')] = 1

    for c1, c2 in zip(str1_chars, str2_chars):
        if c1 and c2:
            print(1)
            break
    else:
        print(0)
