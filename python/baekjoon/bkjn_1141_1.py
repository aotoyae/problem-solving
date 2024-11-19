import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

words.sort(key=len)
cnt = 0

for i in range(N):
    answer = False

    for j in range(i + 1, N):
        if words[i] == words[j][0:len(words[i])]:
            answer = True
            break
    if not answer:
        cnt += 1

print(cnt)