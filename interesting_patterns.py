# http://practice.geeksforgeeks.org/problems/interesting-patterns/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    numbr = int(input().strip())
    x = 2 * numbr - 2
    for trk in range(x + 1):
        for trk2 in range(x + 1):
            print(numbr - (min(min(abs(trk - x), trk), min(abs(trk2 - x), trk2))), end='')
        print(end=' ')
    print()
        
