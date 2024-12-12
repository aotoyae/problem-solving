import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, K = map(int, input().split())
lst = [i for i in range(1, N + 1)]

answer = []
num = 0

for i in range(N):
    num += K - 1

    if num >= len(lst):
        num %= len(lst)

    answer.append(str(lst.pop(num)))

print(f"<{', '.join(answer)}>")
