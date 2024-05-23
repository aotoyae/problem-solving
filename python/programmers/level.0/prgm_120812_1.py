def solution(array):
    dic = {}
    
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    max_value = max(dic.values())
    max_keys = [key for key in dic if dic[key] == max_value]

    return max_keys[0] if len(max_keys) == 1 else -1