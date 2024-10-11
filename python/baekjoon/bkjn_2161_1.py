import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
lst = list(range(1, N + 1))

for _ in range(N - 1):
    print(lst.pop(0))
    num = lst.pop(0)
    lst.append(num)

print(lst[0])