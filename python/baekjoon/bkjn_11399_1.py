import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = sorted(map(int, input().split()))
time = 0
x = 0

for num in lst:
    x += num
    time += x

print(time)
