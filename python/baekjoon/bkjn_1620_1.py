import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
dic = {}

for i in range(N):
    name = input().strip()
    lst.append(name)
    dic[name] = i + 1

for _ in range(M):
    v = input().strip()
    if v.isdigit():
        print(lst[int(v) - 1])
    else:
        print(dic[v])