import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    word = (input().strip())
    if word not in arr:
        arr.append(word)

arr.sort(key=lambda x: (len(x), x))

for i in arr:
    print(i)