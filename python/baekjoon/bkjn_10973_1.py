import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(lst)

if lst == sorted_lst:
    print(-1)

for i in range(N - 1, 0, -1):
    if lst[i] < lst[i - 1]:
        x, y = i - 1, i

        for j in range(N - 1, 0, -1):
            if lst[j] < lst[x]:
                lst[j], lst[x] = lst[x], lst[j]
                lst = lst[:i] + sorted(lst[i:], reverse=True)
                print(*lst)
                exit(0)