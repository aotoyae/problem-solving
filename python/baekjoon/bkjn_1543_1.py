import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

doc = input().strip()
word = input().strip()
idx = 0
cnt = 0

while idx <= len(doc) - len(word):
    if doc[idx:idx + len(word)] == word:
        cnt += 1
        idx += len(word)
    else:
        idx += 1

print(cnt)