import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
set_lst = set()
cnt = 0

for _ in range(N):
    name = input().strip()

    if name == "ENTER":
        set_lst = set()
    else:
        if name not in set_lst:
            set_lst.add(name)
            cnt += 1

print(cnt)