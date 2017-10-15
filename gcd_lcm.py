# http://practice.geeksforgeeks.org/problems/lcm-and-gcd/0
test_cases = int(input().strip())


def find_gcd(a, b):
    if a == b:
        return a

    if a > b:
        return find_gcd(a - b, b)
    else:
        return find_gcd(a, b - a)


for a_tc in range(test_cases):
    ab = input().strip().split()
    ab = [int(i) for i in ab]
    a, b = ab[0], ab[1]
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    print(lcm, gcd)
