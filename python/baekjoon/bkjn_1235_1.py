import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
nums = [input().strip() for _ in range(N)]

for i in range(1, len(nums[0]) + 1):
    lst = []

    for j in range(N):
        if nums[j][-i:] in lst:
            break
        else:
            lst.append(nums[j][-i:])

    if len(lst) == N:
        print(i)
        break