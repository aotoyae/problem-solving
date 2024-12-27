import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
num = 1

for i in range(N, 1, -1):
    num *= i

lst = list(map(int, str(num)))[::-1]

for i in lst:
    if i == 0:
        continue
    else:
        print(i)
        break
        