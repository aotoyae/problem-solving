import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

lst = [-1] * 10001
lst[1] = 1 #SK
lst[2] = 0 #CY
lst[3] = 1 #SK

for i in range(4, N + 1):
    if lst[i - 1] == 1 or lst[i - 3] == 1:
        lst[i] = 0
    else:
        lst[i] = 1

if lst[N] == 1:
    print('SK')
else:
    print('CY')
