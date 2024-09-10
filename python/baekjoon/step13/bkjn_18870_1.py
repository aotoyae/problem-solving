import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


n = int(input())
lst = list(map(int, input().split()))
set_lst = sorted(list(set(lst)))

dic = {set_lst[i]: i for i in range(len(set_lst))}

for i in lst:
    print(dic[i], end=' ')
