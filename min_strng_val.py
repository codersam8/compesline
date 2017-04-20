#http://practice.geeksforgeeks.org/problems/minimize-string-value/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    ip_str = input().strip()
    red_cnt = int(input().strip())
    freq_dic = {}
    
    for a_char in ip_str:
        if a_char in freq_dic:
            freq_dic[a_char] += 1
        else:
            freq_dic[a_char] = 1
    # print('*' * 80)
    # print('first', freq_dic)
    for trk in range(red_cnt):
        max_key = None
        max_val = 0

        for key in freq_dic:
            if freq_dic[key] > max_val:
                max_key = key
                max_val = freq_dic[key]

        freq_dic[max_key] -= 1
    # print('*' * 80)
    # print('after red', freq_dic)
    val = 0
    for key in freq_dic:
        val += freq_dic[key] ** 2

    print(val)
        
