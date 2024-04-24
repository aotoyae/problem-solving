def solution(babbling):
    a = ['aya','ye','woo','ma']
    count = 0

    for i in babbling:
        result = 0
        for j in range(4):
            if i.find(a[j]) != -1:
                result += len(a[j])
        if len(i) == result:
            count += 1

    return count