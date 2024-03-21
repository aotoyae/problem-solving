def solution(array, n):
    arr = []
    arr2 = []

    for i in array:
        arr.append(abs(n-i))
    
    for j in range(len(arr)):
        if arr[j] == min(arr):
            arr2.append(array[j])

    return min(arr2)