import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

dic = {}
lst = []

for _ in range(12):
    x, y = map(int, input().split())

    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]

    if y in dic:
        dic[y].append(x)
    else:
        dic[y] = [x]

for i in dic:
    if len(dic[i]) == 3:
        lst.append(i)

for i in lst:
    cnt = 0

    for j in dic[i]:
        cnt += len(dic[j])
    if cnt == 6:
        print(i)
        break
