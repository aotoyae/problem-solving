def solution(food):
    answer = ""

    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    return f"{answer}0{answer[::-1]}"
        