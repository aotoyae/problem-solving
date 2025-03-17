import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    lst = list(map(float, input().split()))
    N, M = 0, 0

    for idx in range(0, 12, 2):
        P = 0
        D = lst[idx] ** 2 + lst[idx + 1] ** 2

        if D <= 9:
            P += 100
        elif 9 < D <= 36:
            P += 80
        elif 36 < D <= 81:
            P += 60
        elif 81 < D <= 144:
            P += 40
        elif 144 < D <= 225:
            P += 20

        if 0 <= idx <= 4:
            N += P
        else:
            M += P

    print(f"SCORE: {N} to {M}, {'TIE' if N == M else 'PLAYER 1 WINS' if N > M else 'PLAYER 2 WINS'}.")