nums = input().split()

num1 = nums[0][::-1]
num2 = nums[1][::-1]

print(num1 if num1 > num2 else num2)