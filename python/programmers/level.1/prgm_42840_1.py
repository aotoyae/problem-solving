def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4 ,5, 5]
    total = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if (first[i % len(first)] == answers[i]): total[0] += 1
        if (second[i % len(second)] == answers[i]): total[1] += 1
        if (third[i % len(third)] == answers[i]): total[2] += 1

    for i in range(len(total)):
        if (total[i] == max(total)): answer.append(i+1)

    return answer