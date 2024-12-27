import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
num = 1

for i in range(N, 1, -1):
    num *= i

num = str(num)[::-1]

for i in num:
    if i != '0':
        print(i)
        break
