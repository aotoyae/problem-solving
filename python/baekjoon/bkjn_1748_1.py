import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = input().strip()
cnt = 0

for i in range(1, len(N)):
    cnt += 9 * 10 ** (i - 1) * i

cnt += (int(N) - 10 ** (len(N) - 1) + 1) * len(N)

print(cnt)