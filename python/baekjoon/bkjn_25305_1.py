import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
print(lst[K - 1])