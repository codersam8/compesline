test_cases = int(input().strip())
for a_tc in range(test_cases):
    nr = input().strip()
    nr = nr.split(' ')
    nr = [int(i) for i in nr]
    fact = 1
    for a_num in range(nr[0] - nr[1] + 1, nr[0] + 1):
        fact *= a_num
    print(fact)
