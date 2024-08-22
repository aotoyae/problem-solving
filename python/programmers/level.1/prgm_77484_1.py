def solution(lottos, win_nums):
    correct = len([num for num in lottos if num  in win_nums])
    zeros = lottos.count(0)

    min = 6 if 7 - correct >= 6 else 7 - correct
    max = 1 if min - zeros < 1 else min - zeros

    return [max, min]