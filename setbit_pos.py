# http://practice.geeksforgeeks.org/problems/find-position-of-set-bit/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    num = int(input().strip())
    # print(num & (num-1))
    if not (num & (num-1)):
        # print(num)
        i = 1
        pos = 1
        while True:
            # print(i)
            if i & num:
                print( pos)
                break
            else:
                pos += 1
                i <<= 1
            
    else:
        print(-1)
