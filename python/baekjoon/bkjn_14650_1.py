import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
cnt = 0

def solution(n, sum):
    global cnt

    if n == N:
        if sum % 3 == 0:
            cnt += 1
        return

    for i in range(3):
        if n == 0 and i == 0:
            continue
        solution(n + 1, sum + i)

solution(0, 0)
print(cnt)