# http://practice.geeksforgeeks.org/problems/print-the-kth-digit/0  
test_cases = int(input().strip())

for a_tc in range(test_cases):
    ip_line = input().strip().split()
    ip_line = [int(i) for i in ip_line]
    a, b, k = ip_line[0], ip_line[1], ip_line[2]
    a_pow_b = a ** b
    k_dig = None
    while a_pow_b > 0 and k > 0:
        k_dig = a_pow_b % 10
        a_pow_b //= 10
        k -= 1
    print(k_dig)
