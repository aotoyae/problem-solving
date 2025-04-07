import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    name = input().strip()

    if len(name) == 3:
        lst.append(name)

lst.sort()
print(lst[0])