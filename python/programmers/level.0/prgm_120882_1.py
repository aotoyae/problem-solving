def solution(score):
    arr = [sum(i) for i in score]
    sorted_arr = sorted(arr, reverse=True)

    return [sorted_arr.index(sum(i))+1 for i in score]