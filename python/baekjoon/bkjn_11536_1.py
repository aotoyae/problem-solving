import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [input().strip() for _ in range(N)]
sorted_lst = sorted(lst)
reversed_lst = sorted_lst[::-1]

if lst == sorted_lst:
    print('INCREASING')
elif lst == reversed_lst:
    print('DECREASING')
else:
    print('NEITHER')