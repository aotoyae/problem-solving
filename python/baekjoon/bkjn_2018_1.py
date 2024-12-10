import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
cnt, total, start, end = 0, 0, 0, 0

while end <= N:
    if total < N:
        end += 1
        total += end
    elif total > N:
        total -= start
        start += 1
    else:
        cnt += 1
        end += 1
        total += end

print(cnt)
