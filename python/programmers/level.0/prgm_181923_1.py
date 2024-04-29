def solution(arr, queries):
    result = []

    for s, e, k in queries:
        tmp = []
        for i in arr[s:e+1]:
            if i > k:
                tmp.append(i)
        result.append(min(tmp) if tmp else -1)

    return result     