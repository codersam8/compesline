# http://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
tc = int(input().strip())


def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def rotate(ip_list, list_len, rot):
    for idx in range(gcd(list_len, rot)):
        temp = ip_list[idx]
        curr_ind = idx

        while True:
            next_ind = curr_ind + rot
            if next_ind >= list_len:
                next_ind = next_ind - list_len
            if next_ind == idx:
                break
            ip_list[curr_ind] = ip_list[next_ind]
            curr_ind = next_ind
        ip_list[curr_ind] = temp

    [print(i, end=' ') for i in ip_list]
    print()


for a_tc in range(tc):
    len_rot = input().strip().split()
    len_rot = [int(i) for i in len_rot]
    ip_len, rot = len_rot[0], len_rot[1]

    ip_list = input().strip().split()
    ip_list = [int(i) for i in ip_list]
    rotate(ip_list, ip_len, rot)
