import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

K = int(input())
inf_num = 10 ** 7
lst = [1] * inf_num

for i in range(2, int(inf_num ** 0.5) + 1):
    if lst[i]:
        for j in range(i + i, inf_num, i):
            lst[j] = 0

prime = [i for i in range(2, inf_num) if lst[i]]
print(prime[K - 1])