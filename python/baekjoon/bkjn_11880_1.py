import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    lst = list(map(int, input().split()))
    max_len = max(lst)
    shortest = (sum(lst) - max_len) ** 2 + max_len ** 2

    print(shortest)