import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    num = input().strip()
    cnt = 0

    for i in num:
        if i.isdigit():
            cnt += int(i)

    lst.append((num, cnt))

lst.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in lst:
    print(i[0])

