import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
cnt = 0

for _ in range(N):
    lst.append(input())

set_lst = set(lst)

for i in range(M):
    word = input()
    if word in set_lst: cnt += 1

print(cnt)