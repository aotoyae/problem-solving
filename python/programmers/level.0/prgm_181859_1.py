def solution(arr):
    stk = []

    for i in range(len(arr)):
        stk.pop() if stk and stk[-1] == arr[i] else stk.append(arr[i])

    return stk or [-1]