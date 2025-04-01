import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

lst = sorted(map(int, input().split()))

print(*lst)