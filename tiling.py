# http://practice.geeksforgeeks.org/problems/ways-to-tile-a-floor/0
test_cases = int(input().strip())

feb_ser = [1, 2]

def find_n_num(n):
    if len(feb_ser) >= n:
        return feb_ser[n - 1]
    else:
        n_num = find_n_num(n - 1) + find_n_num(n - 2)
        feb_ser.append(n_num)
        return n_num

for a_tc in range(test_cases):
    n = int(input().strip())
    n_num = find_n_num(n)
    print(n_num)
    
