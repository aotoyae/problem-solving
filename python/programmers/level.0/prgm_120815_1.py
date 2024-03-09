def solution(n):
    piece = 6
    answer = 1

    while piece%n != 0:
        piece += 6
        answer += 1

    return answer