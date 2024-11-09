import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [input().strip() for _ in range(N)]

for i in range(N):
    dq = deque(lst[i])

    while True:
        dq.append(dq.popleft())
        word = ''.join(dq)

        if word == lst[i]:
            break
        if word in lst:
            idx = lst.index(word)
            lst.pop(idx)
            lst.insert(idx, lst[i])

lst = set(lst)
print(len(lst))
