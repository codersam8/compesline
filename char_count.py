test_cases = int(input().strip())
# print("test_cases " + str(test_cases))
for i in range(test_cases):
    sent = input().strip()
    char_count = 0
    for a_char in sent:
        if ord('a') <= ord(a_char) <= ord('z') or ord('A') <= ord(a_char) <= ord('Z'):
            char_count += 1
    print(char_count)
