s = input('please enter the string ')
for i in range(len(s)):
    k = s[i+1:]
    for n in range(len(k)):
        if s[i] == k[n]:
            break
    else:
        print(s[i])
        break