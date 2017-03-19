#http://www.practice.geeksforgeeks.org/editorial.php?pid=395
test_cases = int(input().strip())
# print("test_cases " + str(test_cases))
for i in range(test_cases):
    numb = int(input().strip())
    parity_count = 0
    # could have used boolean and not instead of int
    while(numb > 0):
        if numb % 2 == 1:
            parity_count += 1

        numb = int(numb / 2)

    if parity_count % 2 == 0:
        print ('even')
    else:
        print ('odd')
