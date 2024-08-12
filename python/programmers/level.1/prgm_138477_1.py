def solution(k, score):
    hall_of_fame = []
    result = []

    for i in score:
        hall_of_fame.append(i)
        hall_of_fame = sorted(hall_of_fame)[::-1][:k]
        result.append(hall_of_fame[-1])

    return result
