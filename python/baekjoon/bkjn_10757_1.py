import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

lst = sum(map(int, input().split()))

print(lst)