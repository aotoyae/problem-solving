def solution(emergency):
    arr_sort = sorted(emergency, reverse=True)
    answer = []

    for i in emergency:
        answer.append(arr_sort.index(i)+1)

    return answer