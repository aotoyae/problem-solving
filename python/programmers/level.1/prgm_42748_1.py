def solution(array, commands):
    answer = []

    for num in commands:
        sliced_arr = sorted(array[num[0]-1:num[1]])
        answer.append(sliced_arr[num[2]-1])

    return answer