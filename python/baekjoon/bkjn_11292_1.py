import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

while True:
    N = int(input())

    if N == 0:
        break

    max_h = 0
    lst = []

    for _ in range(N):
        n, h = input().split()
        h = float(h)

        if h > max_h:
            max_h = h
            lst = [n]
        elif h == max_h:
            lst.append(n)

    print(*lst)