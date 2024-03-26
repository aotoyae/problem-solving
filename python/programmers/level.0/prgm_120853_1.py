def solution(s):
    arr = s.split(' ')
    num = 0

    for i in range(len(arr)):
        if arr[i] == 'Z':
            num -= int(arr[i-1])
        else:
            num += int(arr[i])

    return num