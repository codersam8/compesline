test_cases = int(input().strip())
max_ind = ord('9')
min_ind = ord('0')
for a_tc in range(test_cases):
    inp_str = input().strip()
    for a_char in inp_str:
        if min_ind <= ord(a_char) <= max_ind:
            print(a_char, end='')
    print()
