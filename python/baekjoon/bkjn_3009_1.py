import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

x_lst = []
y_lst = []

for _ in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

for i in range(3):
    if x_lst.count(x_lst[i]) == 1:
        x = x_lst[i]
    if y_lst.count(y_lst[i]) == 1:
        y = y_lst[i]

print(x, y)