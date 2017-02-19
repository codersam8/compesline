# http://www.practice.geeksforgeeks.org/problem-page.php?pid=527
test_cases = int(input().strip())
# print("test_cases " + str(test_cases))
for i in range(test_cases):
    num = int(input())
    for curr_num in range(1, num + 1):
        for a_num in range(1, curr_num):
            print(a_num, end='')
        for a_num in range(curr_num, 0, -1):
            print(a_num, end='')
        print(' ', end='')
    print()
