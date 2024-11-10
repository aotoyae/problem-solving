import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(101)]
dic = [{} for _ in range(101)]
cnt = 0

for i in range(N):
    num = 0
    word = input().strip()

    for j in word:
        if j not in dic[i]:
            dic[i][j] = str(num)
            num += 1

        lst[i] += dic[i][j]

for i in range(N):
    for j in range(i + 1, N):
        if lst[i] == lst[j]:
            cnt += 1

print(cnt)
