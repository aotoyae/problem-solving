import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    name, point = input().split()
    lst.append((name, int(point)))

sorted_lst = sorted(lst, key=lambda x: (-x[1], x[0]))
print(sorted_lst[0][0])