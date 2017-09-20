# http://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
tc = int(input().strip())

perm_list = []


def permute(ip_str, l, r):
    if l == r:
        perm_list.append(''.join(ip_str))
    else:
        for idx in range(l, (r + 1)):
            ip_str[idx], ip_str[l] = ip_str[l], ip_str[idx]
            permute(ip_str, (l + 1), r)
            ip_str[l], ip_str[idx] = ip_str[idx], ip_str[l]


for a_tc in range(tc):
    perm_list = []
    ip_str = input().strip()
    ip_str = list(ip_str)
    ip_len = len(ip_str)
    permute(ip_str, 0, (ip_len - 1))
    perm_list.sort()
    for a_str in perm_list:
        print(a_str, end=' ')
    print()
