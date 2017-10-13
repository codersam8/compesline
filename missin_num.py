tc = int(input().strip())

for a_tc in range(tc):
    ip_len = int(input().strip())
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    all_sum = (ip_len * (ip_len + 1)) // 2
    for a_num in num_list:
        all_sum -= a_num
    print(all_sum)
