# http://practice.geeksforgeeks.org/problems/boolean-matrix-problem/0
tc = int(input().strip())

for a_tc in range(tc):
    rc = input().strip().split()
    r, c = int(rc[0]), int(rc[1])
    # print(r, c)
    ip_row = input().strip().split()
    ip_row = [int(i) for i in ip_row]
    # print(ip_row)
    mat = []
    for a_r in range(r):
        mat.append(ip_row[(a_r * c):((a_r * c) + c)])
    # print(mat)
    row_flag = False
    col_flag = False
    for a_c in range(c):
        if mat[0][a_c]:
            row_flag = True

    for a_r in range(r):
        if mat[a_r][0]:
            col_flag = True

    for a_r in range(1, r):
        for a_c in range(1, c):
            if mat[a_r][a_c]:
                mat[0][a_c] = 1
                mat[a_r][0] = 1
    # for filling columns
    for a_c in range(1, c):
        if mat[0][a_c]:
            for a_r in range(1, r):
                mat[a_r][a_c] = 1

    # for filling rows
    for a_r in range(1, r):
        if mat[a_r][0]:
            for a_c in range(1, c):
                mat[a_r][a_c] = 1

    if row_flag:
        for a_c in range(c):
            mat[0][a_c] = 1

    if col_flag:
        for a_r in range(r):
            mat[a_r][0] = 1

    for a_r in range(r):
        for a_c in range(c):
            print(mat[a_r][a_c], end=' ')
    print()
