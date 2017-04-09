# http://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0

test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    no_of_packets = int(input().strip())
    packets = input().strip().split(' ')
    packets = [int(i) for i in packets]
    students = int(input().strip())
    packets = sorted(packets)
    # print('*' * 80)
    # print('packets', packets)

    min_chocs = packets[no_of_packets - 1]
    for trk in range(no_of_packets - students + 1):
        # print('*' * 80)
        # print('', packets[trk], packets[trk + students - 1])
        current_diff = abs(packets[trk] - packets[trk + students - 1])
        # print('current_diff', current_diff)
        if current_diff < min_chocs:
            min_chocs = current_diff

    print(min_chocs)
