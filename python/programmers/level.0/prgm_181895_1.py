def solution(arr, intervals):
    answer = []

    a, b = intervals[0]
    c, d = intervals[1]
    answer += arr[a:b+1]
    answer += arr[c:d+1]

    return answer