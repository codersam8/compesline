test_cases = int(input().strip())

for a_tc in range(test_cases):
    str1, str2 = input().strip().split()
    # print(str1, str2)
    eve_ch = [0] * 26
    odd_ch = [0] * 26

    if len(str1) != len(str2):
        print(0)
        continue

    for chr1, chr2, idx in zip(str1, str2, range(len(str1))):
        if idx % 2 == 0:
            eve_ch[ord(chr1) - ord('a')] += 1
            eve_ch[ord(chr2) - ord('a')] -= 1
        else:
            odd_ch[ord(chr1) - ord('a')] += 1
            odd_ch[ord(chr2) - ord('a')] -= 1

    for val1, val2 in zip(eve_ch, odd_ch):
        if val1 or val2:
            print(0)
            break
    else:
        print(1)
