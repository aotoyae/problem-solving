import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
m = int(input())
dic = {}
f_lst = []

for i in range(m):
    f, ff = map(int, input().split())

    if f not in dic:
        dic[f] = []
    if ff not in dic:
        dic[ff] = []

    dic[f].append(ff)
    dic[ff].append(f)

# print(dic)

if 1 in dic:
    for i in dic[1]:
        f_lst.append(i)

        if i in dic:
            for j in dic[i]:
                f_lst.append(j)

f_lst = set(f_lst)
print(max(len(f_lst) - 1, 0))