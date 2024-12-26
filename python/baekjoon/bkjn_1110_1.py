import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
new_N = N
cnt = 0

while True:
    a = new_N // 10
    b = new_N % 10
    c = (a + b) % 10
    new_N = (b * 10) + c

    cnt += 1

    if N == new_N:
        break
print(cnt)