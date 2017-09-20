# http://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos/0
tc = int(input().strip())

for a_tc in range(tc):
    ip_len = int(input().strip())
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    pos_list = []
    neg_list = []
    pos_len = 0
    neg_len = 0
    for trk in num_list:
        if trk >= 0:
            pos_list.append(trk)
            pos_len += 1
        else:
            neg_list.append(trk)
            neg_len += 1
    # print('*' * 80)
    # print('pos_list', pos_list)
    # print('*' * 80)
    # print('neg_list', neg_list)

    pos_ind = 0
    neg_ind = 0
    for idx in range(ip_len):
        if (idx // 2) == len(pos_list) or (idx // 2) == len(neg_list):
            break
        if idx % 2 == 0:
            num_list[idx] = pos_list[pos_ind]
            pos_ind += 1
        else:
            num_list[idx] = neg_list[neg_ind]
            neg_ind += 1

    if len(pos_list) > len(neg_list):
        idx1 = pos_ind
        rem_list = pos_list
    else:
        idx1 = neg_ind
        rem_list = neg_list
    while idx < (ip_len) and idx1 < len(rem_list):
        # print('*' * 80)        
        num_list[idx] = rem_list[idx1]
        idx += 1
        idx1 += 1

    for a_num in num_list:
        print(a_num, end=' ')
    print()
