def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    answer = []

    for i in photo:
        count = 0
        
        for j in i:
            if j in score: count += score[j]
        
        answer.append(count)

    return answer
    