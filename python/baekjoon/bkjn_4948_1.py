import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

num = 123456 * 2 + 1
lst = [1] * num

for i in range(2, num):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            lst[i] = 0
            break

while True:
    n = int(input())
    prime = 0

    if n == 0: break

    for i in range(n + 1, 2 * n + 1):
        prime += lst[i]

    print(prime)