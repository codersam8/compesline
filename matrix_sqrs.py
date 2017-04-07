test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    dims = input().strip().split(' ')
    dims = [int(i) for i in dims]

    m, n = dims[0], dims[1]

    if m < n:
        m, n = n, m

    total_squares = int((n * (n + 1) * (2 * n + 1) / 6 ) +
                     (m - n) * n * (n + 1) / 2 )
    print(total_squares)
