# practice.geeksforgeeks.org/problems/sieve-of-eratosthenes/0/
test_cases = int(input().strip())
lim_list = []
for a_tc in range(test_cases):
    lim_list.append(int(input().strip()))
biggest = max(lim_list)
sieve_list = [True] * (biggest + 1)

val = 2
# need to check why this is necessary
while val ** 2 <= biggest:
    if sieve_list[val]:
        for val2 in range((2*val), biggest + 1, val):
            sieve_list[val2] = False
    val += 1

for lim in lim_list:
    for val in range(2, lim + 1):
        if sieve_list[val]:
            print(val, end=' ')
    print()
