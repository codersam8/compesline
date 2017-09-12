# http://practice.geeksforgeeks.org/problems/remove-spaces/0
tc = int(input().strip())

for a_tc in range(tc):
    ip_str = input()
    ip_str = list(ip_str)
    str_len = 0
    for trk in range(len(ip_str)):
        if ip_str[trk] != ' ':
            ip_str[str_len] = ip_str[trk]
            str_len += 1
    ip_str = ip_str[:str_len]
    ip_str = ''.join(ip_str)
    print(ip_str)
