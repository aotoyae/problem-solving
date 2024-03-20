def solution(my_string):
    nums = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in nums.split())