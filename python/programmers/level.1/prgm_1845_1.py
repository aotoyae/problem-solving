def solution(nums):
    set_list = set(nums)
    limit = len(nums)/2

    return limit if len(set_list) > limit else len(set_list)
