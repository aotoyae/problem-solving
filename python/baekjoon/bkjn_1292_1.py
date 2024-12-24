import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

A, B = map(int, input().split())
lst = [0]
cnt = 1

while len(lst) <= B:
    lst += [cnt] * cnt
    cnt += 1

print(sum(lst[A:B + 1]))