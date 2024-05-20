def solution(n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    row = 0
    col = 0
    num = 1

    for i in range(n, 0, -2):
        for _ in range(i):
            result[row][col] = num
            col += 1
            num += 1
        col -= 1
        row += 1

        for _ in range(i-1):
            result[row][col] = num
            row += 1
            num += 1
        col -= 1
        row -= 1

        for _ in range(i-1):
            result[row][col] = num
            col -= 1
            num += 1
        col += 1
        row -= 1

        for _ in range(i-2):
            result[row][col] = num
            row -= 1
            num += 1
        col += 1
        row += 1
    
    return result

