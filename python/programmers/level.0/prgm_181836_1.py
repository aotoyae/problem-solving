def solution(picture, k):
    result = []

    for i in range(len(picture)):
        paint = ""

        for j in range(len(picture[i])):
            paint += picture[i][j] * k
        
        for _ in range(k):
            result.append(paint)

    return result