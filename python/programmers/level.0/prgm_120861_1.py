def solution(keyinput, board):
    result = [0, 0]
    row = board[0] / 2
    column = board[1] / 2

    for i in range(len(keyinput)):
        if keyinput[i] == "left" and result[0] - 1 > -row:
            result[0] -= 1
        if keyinput[i] == "right" and result[0] + 1 < row:
            result[0] += 1
        if keyinput[i] == "up" and result[1] + 1 < column:
            result[1] += 1
        if keyinput[i] == "down" and result[1] - 1 > -column:
            result[1] -= 1
            
    return result