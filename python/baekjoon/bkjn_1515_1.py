import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

num = input().strip()
cnt = 0
idx = 0

while True:
    cnt += 1

    for i in str(cnt):
        if num[idx] == i:
            idx += 1

            if idx >= len(num):
                print(cnt)
                exit()
