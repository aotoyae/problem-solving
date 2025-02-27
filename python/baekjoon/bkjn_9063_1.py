import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
n_lst, e_lst = [], []

for _ in range(N):
    n, e = map(int, input().split())

    n_lst.append(n)
    e_lst.append(e)

result = (max(n_lst) - min(n_lst)) * (max(e_lst) - min(e_lst))
print(result)