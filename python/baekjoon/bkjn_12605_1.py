import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

for i in range(N):
    case = input().split()

    print(f"Case #{i + 1}: {' '.join(case[::-1])}")