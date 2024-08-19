def solution(name, yaerning, photo):
    score = {}
    answer = []

    for k, v in zip(name, yaerning):
        score[k] = v

    for i in photo:
        count = 0
        
        for j in i:
            if j in score: count += score[j]
        
        answer.append(count)

    return answer
    