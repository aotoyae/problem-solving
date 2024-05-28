def solution(n):
    arr = [int(i) for i in str(n)]
    arr.sort(reverse=True)
    answer = ''

    for i in arr:
        answer += str(i)

    return int(answer)
