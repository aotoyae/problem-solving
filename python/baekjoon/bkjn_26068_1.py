import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(N):
    coupon = input()[2:]
    d_day = int(coupon)

    if d_day <= 90:
        cnt += 1

print(cnt)
