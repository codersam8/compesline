test_cases = int(input().strip())

for a_tc in range(test_cases):

    ip_str =  input().strip()
    # print(ip_str)
    que = [list(ip_str)]
    while len(que) > 0:
        ip_str = que[0]
        del que[0]
        # print(ip_str)
        try:
            idx = ip_str.index('?')
        except:
            idx = -1

        if idx != -1:
            ip_str = ip_str[:]
            ip_str[idx] = '0'
            que.append(ip_str)
            ip_str = ip_str[:]
            ip_str[idx] = '1'
            que.append(ip_str)
        else:
            print(''.join(ip_str), end=' ')
    print()
        
    
