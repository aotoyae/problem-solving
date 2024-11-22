import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

for m in range(1, N + 1):
    nums_sum = sum(map(int, str(m))) + m

    if nums_sum == N:
        print(m)
        break

else:
    print(0)