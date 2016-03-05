# https://www.hackerearth.com/problem/algorithm/trailing-zeros/
num = int(raw_input())
zeroes = num / 5
print('*'*80)
print('num / 5')
print(zeroes)
fiveMultiple = 25
fivePowerOneLess = 1
while num / fiveMultiple >= 1:
    zeroes += fivePowerOneLess
    num2 = 2
    while fiveMultiple * num2 <= num and num2 < 5:
        zeroes += fivePowerOneLess
        num2 += 1
    print 'fiveMultiple'
    print fiveMultiple
    fiveMultiple *= 5
    fivePowerOneLess += 1
print('*'*80)
print('num fiveMultiple')
print(zeroes)
tenMultiple = 100
tenPowerOneLess = 1
while num / tenMultiple >= 1:
    zeroes += tenPowerOneLess
    num2 = 2
    while tenMultiple * num2 <= num and num2 < 10:
        zeroes += tenPowerOneLess
        num2 += 1
    print 'tenMultiple'
    print tenMultiple
    tenMultiple *= 10
    tenPowerOneLess += 1
print('*'*80)
print('num tenMultiple')
print(zeroes)
