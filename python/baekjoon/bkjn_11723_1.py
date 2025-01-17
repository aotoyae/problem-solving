import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    order = input().split()

    if len(order) == 1:
        if order[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        o, x = order[0], int(order[1])

        if o == 'add':
            S.add(x)
        elif o == 'remove':
            S.discard(x)
        elif o == 'check':
            print(1) if x in S else print(0)
        elif o == 'toggle':
            S.discard(x) if x in S else S.add(x)