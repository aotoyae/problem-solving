import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

print(round(sum(lst) / N))
print(lst[N // 2])

dic = dict()

for i in lst:
    if i in dic: dic[i] += 1
    else: dic[i] = 1

mx = max(dic.values())
mx_lst = []

for i in dic:
    if dic[i] == mx:
        mx_lst.append(i)

print(mx_lst[0]) if len(mx_lst) == 1 else print(mx_lst[1])
print(lst[-1] - lst[0])