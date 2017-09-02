# http://practice.geeksforgeeks.org/problems/bit-difference/0
tc = int(input().strip())
for a_tc in range(tc):
    a_b = input().strip().split()
    a_b = [int(i) for i in a_b]
    a, b = a_b[0], a_b[1]
    res = a ^ b
    flips = 0
    while res:
        flips += (res & 1)
        res >>= 1
    print(flips)
