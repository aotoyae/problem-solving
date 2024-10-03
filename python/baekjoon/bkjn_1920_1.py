import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
first_lst = set(map(int, input().split()))
M = int(input())
second_lst = list(map(int, input().split()))

for i in second_lst:
    print(1) if i in first_lst else print(0)