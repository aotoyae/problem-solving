import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
st = sorted(set(lst))

print(*st)