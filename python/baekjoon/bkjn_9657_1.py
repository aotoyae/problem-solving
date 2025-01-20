import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [1, 1, 0, 1, 1]

for i in range(5, N + 1):
    if lst[i - 1] + lst[i - 3] + lst[i - 4] == 3:
        lst.append(0)
    else:
        lst.append(1)

if lst[N] == 0:
    print('CY')
else:
    print('SK')