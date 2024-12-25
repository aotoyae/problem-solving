import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
total = 0

for i in range(1, N):
    total += N * i + i

print(total)