import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
lst = []

for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
            num = nums[i] + nums[j] + nums[k]
            if num <= M:
                lst.append(num)

print(max(lst))