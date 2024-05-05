def solution(arr, k):
    answer = []

    for i in arr:
        if len(answer) < k and i not in answer:
            answer.append(i)
    
    return answer + [-1] * (k - len(answer))