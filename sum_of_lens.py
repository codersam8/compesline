# https://practice.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    list_len = int(input().strip())
    a_list = input().strip().split()
    a_list = [int(i) for i in a_list]
    max_ele = int(input().strip())
    # print('*' * 80)
    # print('a_list max_ele', a_list, max_ele)

    trk = 0
    tot = 0
    count = 0
    found = False

    while trk < list_len:
        if a_list[trk] < max_ele:
            count += 1
        elif a_list[trk] == max_ele:
            found = True
            count += 1
        else:
            # print('*' * 80)
            # print('in last condition', found)
            if found:
                tot += count
                found = False
            count = 0
            # print('tot', tot)
        # print('*' * 80)
        # print('count', count)
        # print('a_list[trk]', a_list[trk])
        # print('found', found)
        trk += 1
        # this is for such situations where loop has crossed the end of items
    if found:
        tot += count
    # print('tot', tot)
    print(tot)
