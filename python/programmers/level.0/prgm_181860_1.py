def solution(arr, flag):
    answer = []

    for i, b in enumerate(flag):
        if b:
            answer += [arr[i]] * (arr[i]*2)
        else:
            answer = answer[:len(answer) - arr[i]]

    return answer