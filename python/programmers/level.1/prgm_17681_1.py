def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin1 = format(arr1[i], 'b')
        bin2 = format(arr2[i], 'b')
        map = ""

        if len(bin1) < n: bin1 = (n - len(bin1)) * "0" + bin1
        if len(bin2) < n: bin2 = (n - len(bin2)) * "0" + bin2

        for j in range(n):
            if bin1[j] == "1" or bin2[j] == "1":
                map += "#"
            else: map += " "
        
        answer.append(map)

    return answer