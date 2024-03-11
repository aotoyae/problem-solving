def solution(a, d, included):
    answer = []

    for i, x in enumerate(included):
        if x:
            answer.append(a + d*i)

    return sum(answer)