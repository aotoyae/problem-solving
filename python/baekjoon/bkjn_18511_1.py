import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from itertools import product

N, K = map(int, input().split())
lst = sorted(list(map(int, input().split())), reverse=True)
length = len(str(N))

while True:
    temp = list(product(lst, repeat=length))
    answer = []

    for i in temp:
        num = int(''.join(map(str, i)))
        if num <= N:
            answer.append(num)

    if len(answer) >= 1:
        print(max(answer))
        break
    else:
        length -= 1
