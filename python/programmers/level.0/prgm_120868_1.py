def solution(sides):
    result = 0
    min_num = min(sides)
    max_num = max(sides)

    for i in range(max_num - min_num + 1, max_num + 1):
        result += 1
    
    for j in range(max_num + 1, min_num + max_num):
        result += 1
        

    return result