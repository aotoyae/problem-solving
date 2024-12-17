import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [1]
prefix = [0, 1]

for _ in range(N):
    q, x, y = map(int, input().split())

    if q == 1:
        cnt = prefix[y] - prefix[x - 1]

        if cnt < (y - x + 1):
            print('No')
            lst.append(0)
        else:
            print('Yes')
            lst.append(1)
    else:
        cnt = prefix[y] - prefix[x - 1]

        if cnt > 0:
            print('No')
            lst.append(0)
        else:
            print('Yes')
            lst.append(1)

    prefix.append(prefix[-1] + lst[-1])