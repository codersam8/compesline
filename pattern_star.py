test_cases = int(input().strip())
# print("test cases " + str(test_cases))
    
for test_case in range(test_cases):
    num = int(input().strip())
    for a_num in range(num):
        print('*' * (a_num + 1), end=' ')
    print()
        
