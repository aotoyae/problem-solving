def solution(nums):
    set_list_len = len(set(nums))
    limit_len = len(nums)/2

    return min(set_list_len, limit_len)
