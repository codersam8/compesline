# http://practice.geeksforgeeks.org/problems/four-elements/0

test_cases = int(input().strip())

for a_tc in range(test_cases):
    len_a = int(input().strip())
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    num_list = sorted(num_list)
    tot = int(input().strip())
    found = False
    for trk1 in range(len_a - 3):
        if found:
            break
        for trk2 in range(trk1 + 1, len_a - 2):
            if found:
                break
            trk3 = trk2 + 1
            trk4 = len_a - 1
            curr_sum = (num_list[trk1] +
                        num_list[trk2] +
                        num_list[trk3] +
                        num_list[trk4])
            while trk3 < trk4:
                if (curr_sum == tot):
                    found = True
                    break
                elif curr_sum > tot:
                    trk4 -= 1
                else:
                    trk3 += 1
                curr_sum = (num_list[trk1] +
                            num_list[trk2] +
                            num_list[trk3] +
                            num_list[trk4])
    if found:
        print(1)
    else:
        print(0)
