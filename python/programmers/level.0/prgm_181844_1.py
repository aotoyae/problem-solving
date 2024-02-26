def solution(arr, delete_list):
    s1 = set(arr)
    s2 = set(delete_list)
    test = list(s1 - s2)
    answer = []
    
    for i in arr:
        if i in test:
            answer.append(i)

    return answer