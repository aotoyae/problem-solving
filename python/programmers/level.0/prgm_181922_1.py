def solution(arr, queries):
    for i in queries:
        s, e, k = i
        for j in range(s, e+1):
            if j%k == 0:
                arr[j] += 1

    return arr