import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
skills = input().strip()
cnt = 0
L_cnt, S_cnt = 0, 0

for skill in skills:
    if skill == 'L':
        L_cnt += 1
    elif skill == 'R':
        if L_cnt > 0:
            cnt += 1
            L_cnt -= 1
        else:
            break
    elif skill == 'S':
        S_cnt += 1
    elif skill == 'K':
        if S_cnt > 0:
            cnt += 1
            S_cnt -= 1
        else:
            break
    else:
        cnt += 1

print(cnt)