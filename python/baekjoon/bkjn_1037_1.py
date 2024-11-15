import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

num = int(input())
lst = list(map(int, input().split()))

print(max(lst) * min(lst))
