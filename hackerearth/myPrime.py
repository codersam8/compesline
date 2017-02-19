# https://www.hackerearth.com/problem/algorithm/my-prime/
count = int(raw_input())
# print range(count)
primes = [0] * count
primesCount = 0
nums = raw_input().split()
for trk in range(count):
    nums[trk] = int(nums[trk])
# for i in range(count):
#     nums[i] = int(raw_input())
#print nums
for trk in range(count):
    currNum = nums[trk]
    if currNum != 0:
        # print "for trk2"
        # print range(count)
        for trk2 in range(count):
            currNum2 = nums[trk2]
            if trk == trk2:
                continue
            # print('currNum')
            # print(currNum)
            # print('currNum2')
            # print trk
            # print trk2
            # print(currNum2)
            if currNum2 != 0:
                # print "in outer if"
                if currNum % currNum2 == 0:
                    # print "in inner if"
                    currNum = 0
                    break
        if currNum != 0:
            primes[primesCount] = currNum
            primesCount += 1
for trk in range(primesCount):
    print primes[trk],
