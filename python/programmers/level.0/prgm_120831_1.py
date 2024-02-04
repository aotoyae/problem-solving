def solution(n):
    arr = 0
    for i in range(2, n + 1, 2):
        arr += i

    return arr