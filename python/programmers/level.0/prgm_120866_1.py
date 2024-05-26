def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    result = n * n
    bomb = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb.append([i, j])
                result -= 1

    if result == 0: return 0

    for x, y in bomb:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = 1
                result -= 1
    
    return result
