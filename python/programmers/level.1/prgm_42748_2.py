def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        sliced_arr = sorted(array[i - 1:j])
        answer.append(sliced_arr[k - 1])

    return answer