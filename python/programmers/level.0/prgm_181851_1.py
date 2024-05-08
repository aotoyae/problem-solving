def solution(rank, attendance):
    result = []

    for i in range(len(rank)):
        if attendance[i]:
            result.append([rank[i], i])
    
    result.sort()
    return result[0][1]*10000 + result[1][1]*100 + result[2][1]