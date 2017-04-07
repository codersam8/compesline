test_cases = int(input().strip())
# print("test cases " + str(test_cases))
for test_case in range(test_cases):
    dvd, dvr = input().strip().split(' ')
    dvd, dvr = int(dvd), int(dvr)
    if dvd < dvr:
        dvd, dvr = dvr, dvd
    while dvd % dvr != 0:
        rem = dvd % dvr
        dvd = dvr
        dvr = rem
    common_dvrs = 1
    for a_dvr in range(2, dvr + 1):
        if dvr % a_dvr == 0:
            common_dvrs += 1
    print(common_dvrs)
