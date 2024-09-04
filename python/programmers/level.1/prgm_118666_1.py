def solution(survey, choices):
    mbti = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    category = ['RT', 'CF', 'JM', 'AN']
    answer = ''

    for i in range(len(survey)):
        if choices[i] < 4: mbti[survey[i][0]] += 4 - choices[i]
        else: mbti[survey[i][1]] += choices[i] - 4
    
    for type in category:
        if mbti[type[0]] > mbti[type[1]]: answer += type[0]
        elif mbti[type[0]] == mbti[type[1]]: answer += sorted(type)[0]
        else: answer += type[1]
    
    return answer