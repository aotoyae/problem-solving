import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

E, S, M = map(int, input().split())
lst = [0, 0, 0]
year = 0

while True:
    year += 1
    if lst[0] == 15:
        lst[0] = 1
    else: lst[0] += 1

    if lst[1] == 28:
        lst[1] = 1
    else: lst[1] += 1

    if lst[2] == 19:
        lst[2] = 1
    else: lst[2] += 1

    if [E, S, M] == lst: break

print(year)

