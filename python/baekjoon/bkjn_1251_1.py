import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

word = input().strip()
words = []

for i in range(1, len(word) - 2):
    for j in range(i + 1, len(word)):
        first = word[:i][::-1]
        second = word[i:j][::-1]
        third = word[j:][::-1]
        words.append(first + second + third)

print(sorted(words)[0])
