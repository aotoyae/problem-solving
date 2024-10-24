import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, K = map(int, input().split())
dq = [i for i in range(1, N + 1)]
idx = 0
lst = []

while dq:
    idx += K - 1

    if idx >= len(dq):
        idx %= len(dq)

    lst.append(str(dq.pop(idx)))

print('<' + ', '.join(lst) + '>')

