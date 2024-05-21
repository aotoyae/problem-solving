def solution(lines):
    result = 0
    line_map = [0 for _ in range(200)]

    for i in range(3):
        left = lines[i][0]
        right = lines[i][1]

        for j in range(left, right):
            line_map[j+100] += 1

    for i in range(len(line_map)):
        if line_map[i] > 1: result += 1

    return result