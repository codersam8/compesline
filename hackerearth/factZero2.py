# https://www.hackerearth.com/problem/algorithm/trailing-zeros/
num = int(raw_input())
fivePow = 5
zeroes = 0
while fivePow <= num:
    fives = num / fivePow
    zeroes += fives
    fivePow *= 5
print zeroes
