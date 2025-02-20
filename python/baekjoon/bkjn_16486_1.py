import sys, math
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

d1 = int(input())
d2 = int(input())

total = (d1 * 2) + (d2 * 2 * math.pi)
print(total)