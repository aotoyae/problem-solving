import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

lst = list(map(int, input().split()))
min_num = min(lst)

while True:
    cnt = 0

    for i in lst:
        if min_num % i == 0:
            cnt += 1
    if cnt > 2:
        break
    min_num += 1

print(min_num)