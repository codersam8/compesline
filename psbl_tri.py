# http://practice.geeksforgeeks.org/problems/count-possible-triangles/0
tc = int(input().strip())

for a_tc in range(tc):
    arr_len = int(input().strip())
    ip_list = input().strip().split()
    ip_list = [int(i) for i in ip_list]
    ip_list.sort()
    # print(ip_list)

    count = 0

    for first in range(arr_len - 2):
        third = first + 2
        for sec in range((first + 1), arr_len - 1):
            while (third < arr_len and
                   (ip_list[first] + ip_list[sec] > ip_list[third])):
                third += 1
            count += (third - sec - 1)
    print(count)
