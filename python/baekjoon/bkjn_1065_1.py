import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, N + 1):
    nums = list(map(int, str(i)))

    if i < 100:
        cnt += 1
    elif nums[0] - nums[1] == nums[1] - nums[2]:
        cnt += 1

print(cnt)