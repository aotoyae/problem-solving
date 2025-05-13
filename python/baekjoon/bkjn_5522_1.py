import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

total = 0

for _ in range(5):
    n = int(input())
    total += n

print(total)