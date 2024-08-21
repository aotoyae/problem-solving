def solution(babbling):
    count = 0
    arr = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        for j in arr:
            if j * 2 not in i:
                i = i.replace(j, " ")
        
        if i.isspace():
            count += 1

    return count