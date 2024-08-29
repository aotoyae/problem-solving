import re

def solution(dartResult):
    answer = 0

    split_dartResult = re.split(r'(S|D|T|\*|#)', dartResult)
    split_dartResult = [item for item in split_dartResult if item != ""]

    for i in range(len(dartResult)):
        if dartResult[i] == "D":
            answer += dartResult[i - 1] ** 2
        elif dartResult[i] == "T":
            answer += dartResult[i - 1] ** 3
        elif dartResult[i] == "*":
            if i >= 4:
                answer += dartResult[i - 1] * 2 + dartResult[i - 2]
        
            

    return split_dartResult
