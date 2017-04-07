from __future__ import print_function
# test_cases = 1
# AEbdd
# AFBji
test_cases = int(raw_input().strip())
# print("test cases " + str(test_cases))
for test_case in range(test_cases):
    sample_str = raw_input().strip()
    # sample_str = "AEbdd"
    sample_str_arr = sorted(sample_str)
    # print(sample_str_arr)
    # new_str_arr = []
    sample_str_len = len(sample_str)
    no_of_caps = 0
    while('a' > sample_str_arr[no_of_caps]):
        no_of_caps += 1
    no_of_smalls = len(sample_str) - no_of_caps
    # print("no_of_smalls " + str(no_of_smalls))
    # print("no_of_caps " + str(no_of_caps))
    time_alt = no_of_caps if no_of_caps < no_of_smalls else no_of_smalls
    # print("time_alt " + str(time_alt))
    # print("Hello")
    for a_idx in range(time_alt):
        print(sample_str_arr[a_idx], end='')
        # print()
        print(sample_str_arr[a_idx + no_of_caps], end='')
    next_chars_idx = time_alt if no_of_caps > no_of_smalls else (2 * time_alt)
    # print()
    # print("next_chars_idx " + str(next_chars_idx))
    for a_idx in range(next_chars_idx, next_chars_idx + (len(sample_str) - (2 * time_alt))):
        print(sample_str_arr[a_idx], end='')
    print()
