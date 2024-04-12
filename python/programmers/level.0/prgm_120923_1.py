import math

def solution(num, total):
    result = []
    average_num = math.ceil(total / num)
    minus_num = math.trunc(num / 2)
    start_num = average_num - minus_num

    for i in range(num):
        result.append(start_num + i)
    
    return result