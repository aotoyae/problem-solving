def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num = num_list[-1] - num_list[-2]
        return [*num_list, num]
    else:
        num = num_list[-1] * 2
        return [*num_list, num]