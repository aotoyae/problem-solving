import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split())) + list(map(int, input().split()))
cnt = 0

def solution(n, prev, total):
    global cnt

    if n == N + 1:
        if total >= M:
            cnt += 1
        return

    for i in range(2):
        for j in range(3):
            if j == prev:
                solution(n + 1, j, total + lst[i * 3 + j] // 2)
            else:
                solution(n + 1, j, total + lst[i * 3 + j])

solution(1, -1, 0)
print(cnt)