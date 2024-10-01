import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
N_lst = set()
M_lst = set()

for _ in range(N):
    N_lst.add(input().strip())

for _ in range(M):
    M_lst.add(input().strip())

lst = N_lst & M_lst
sorted_lst = sorted(lst)

print(len(sorted_lst))

for name in sorted_lst:
    print(name)