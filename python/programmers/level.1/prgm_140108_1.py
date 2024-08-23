def solution(s):
    x = ""
    x_count = 0
    y_count = 0
    answer = 0

    for char in s:
        if not x: x = char
        if x == char: x_count += 1
        else: y_count += 1

        if x_count == y_count:
            answer += 1
            x_count, y_count, x = 0, 0, ""

    if x: answer += 1
    
    return answer