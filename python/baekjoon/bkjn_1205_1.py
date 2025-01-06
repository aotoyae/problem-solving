import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, T, P = map(int, input().split())

if N == 0:
    print(1)
else:
    lst = list(map(int, input().split()))

    if N == P and lst[-1] >= T:
        print(-1)
    else:
        grade = N + 1

        for i in range(N):
            if lst[i] <= T:
                grade = i + 1
                break
        print(grade)