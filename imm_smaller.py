# http://www.practice.geeksforgeeks.org/problem-page.php?pid=525
test_cases = int(input().strip())
for a_test_case in range(test_cases):
    input().strip()
    nums_list = input().strip().split(' ')
    nums_list = [int(i) for i in nums_list]
    for a_trk in range(len(nums_list) - 1):
        if(nums_list[a_trk] > nums_list[a_trk + 1]):
            print (nums_list[a_trk + 1], end=' ')
        else:
            print('-1 ', end='')
    print('-1')
        
