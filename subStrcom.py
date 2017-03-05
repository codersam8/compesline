test_cases = int(raw_input().strip())
# print("test cases " + str(test_cases))
for test_case in range(test_cases):
    sub_str = raw_input().strip()[::-1]
    full_str = raw_input().strip()[::-1]
    sub_str_len = len(sub_str)
    sub_str_len_counter = 0
    sub_str_exists = False
    
    c = 0
    while(c < len(full_str)):
        for d in range(len(sub_str)):
            # print("full_str " + full_str[c] + " sub_str " + sub_str[d])
            if c < len(full_str) and full_str[c] == sub_str[d]:
                sub_str_len_counter += 1
                # d += 1
                c += 1
            else:
                c = c - sub_str_len_counter + 1
                # c += 1
                break
            # c += 1
                
        if sub_str_len_counter == sub_str_len:
            print(len(full_str) - c + 1)
            sub_str_exists = True
            break
        else:
            sub_str_len_counter = 0
    if not sub_str_exists:
        print (str(-1))
                
