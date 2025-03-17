import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
SCORE_TABLE = [
    (9, 100), (36, 80), (81, 60), (144, 40), (225, 20)
]

for _ in range(T):
    lst = list(map(float, input().split()))
    N, M = 0, 0

    for idx in range(6):
        D = lst[idx] ** 2 + lst[idx + 1] ** 2
        P = next((score for r, score in SCORE_TABLE if D <= r), 0)

        if idx < 3:
            N += P
        else:
            M += P

    result = 'TIE' if N == M else 'PLAYER 1 WINS' if N > M else 'PLAYER 2 WINS'
    print(f"SCORE: {N} to {M}, {result}.")