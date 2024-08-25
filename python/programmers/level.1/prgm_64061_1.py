def solution(board, moves):
    bucket = []
    count = 0

    for i in moves:
        for j in board:
            if j[i - 1] != 0:
                if bucket and bucket[-1] == j[i - 1]:
                    bucket.pop()
                    count += 2 
                else: bucket.append(j[i - 1])
                j[i - 1] = 0
                break
                

    return count
                        