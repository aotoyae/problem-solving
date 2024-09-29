import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
set_lst = set([])

for _ in range(n):
    name, type = input().split()

    if type == "enter": set_lst.add(name)
    else: set_lst.remove(name)

lst = sorted(set_lst, reverse=True)

for i in range(len(lst)):
    print(lst[i])
