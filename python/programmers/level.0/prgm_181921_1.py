def solution(l, r):
    answer = []

    for i in range(l, r+1):
        num = str(i)
        if all(x == "5" or x == "0" for x in [*num]):
            answer.append(i)
        
    return answer if len(answer) > 0 else [-1]