import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    books = list(map(int, input().split()))
    weight = 0
    cnt = 1

    for book in books:
        if book + weight <= M:
            weight += book
        else:
            weight = book
            cnt += 1

    print(cnt)