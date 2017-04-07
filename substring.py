test_cases = int(raw_input().strip())
# print("test cases " + str(test_cases))
for test_case in range(test_cases):
    input()
    string = input().strip()
    if string == string[::-1]:
        print(1)
    else:
        print(0)
