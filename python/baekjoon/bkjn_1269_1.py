import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
first = set(map(int, input().split()))
second = set(map(int, input().split()))

print(len(first - second) + len(second - first))