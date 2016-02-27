# https://www.hackerearth.com/problem/algorithm/trailing-zeros/
num = int(raw_input())
zeroes = num / 5

fiveMultiple = 25
fivePowerOneLess = 1
while num / fiveMultiple >= 1:
    zeroes += fivePowerOneLess
    fiveMultiple *= 5
    fivePowerOneLess += 1
print zeroes
