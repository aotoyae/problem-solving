import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
MAX = 1000000
is_prime = [1] * (MAX + 1)
is_prime[0] = is_prime[1] = 0

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = 0

for _ in range(T):
    N = int(input())
    cnt = 0

    for i in range(2, N // 2 + 1):
        if is_prime[i] and is_prime[N - i]:
            cnt += 1

    print(cnt)

