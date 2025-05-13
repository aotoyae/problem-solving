import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

lst = map(int, input().split())
total = 0

for i in lst:
    total += i * i

print(total % 10)