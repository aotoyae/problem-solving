def solution(dartResult):
    num = ''
    score = []

    for i in dartResult:
        if i.isdigit():
            num += i
        elif i == "S":
            score.append(int(num))
            num = ""
        elif i == "D":
            score.append(int(num) ** 2)
            num = ""
        elif i == "T":
            score.append(int(num) ** 3)
            num = ""
        elif i == "*":
            if len(score) > 1:
                score[-2:] = [n * 2 for n in score[-2:]]
            else:
                score[0] *= 2 
        elif i == "#":
            score[-1] *= -1
    
    return sum(score)