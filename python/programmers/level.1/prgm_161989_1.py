def solution(n, m, section):
    answer = 0
    paint = 0

    for num in section:
        if num > paint:
            paint = num + m - 1
            answer += 1

    return answer