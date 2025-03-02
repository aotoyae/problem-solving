import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

lst = sorted(map(int, input().split()))
answer = lst[0] + lst[1] + min(lst[2], lst[0] + lst[1] - 1)

print(answer)