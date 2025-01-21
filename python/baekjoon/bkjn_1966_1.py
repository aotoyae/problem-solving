import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 1

    while lst:
        if lst[0] < max(lst):
            lst.append(lst.pop(0))
        else:
            if M == 0:
                break
            lst.pop(0)
            cnt += 1

        M = M - 1 if M > 0 else len(lst) - 1

    print(cnt)
