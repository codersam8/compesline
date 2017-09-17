# http://practice.geeksforgeeks.org/problems/swap-two-nibbles-in-a-byte/0
tc = int(input().strip())

for a_tc in range(tc):
    a_num = int(input().strip())
    first4 = a_num & 0x0f
    first4 <<= 4
    last4 = a_num & 0xf0
    last4 >>= 4
    res = first4 | last4
    print(res)
