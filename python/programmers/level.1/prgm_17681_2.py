def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_map = format(arr1[i]|arr2[i], 'b').rjust(n,'0').replace("1", "#").replace("0", " ")
        answer.append(bin_map)

    return answer