import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b, c = sorted(map(int, input().split()))
    answer = c * c == a * a + b * b

    print(f'Scenario #{i + 1}:')
    print('yes' if answer else 'no')
    print('')