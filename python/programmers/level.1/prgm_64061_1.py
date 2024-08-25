def solution(board, moves):
    bucket = []
    count = 0

    for i in moves:
        for  j in board[i - 1]:
            for k in j:
                if k == 0: continue
                else:
                    if bucket[-1] == k:
                        bucket.pop()
                        count += 2 
                    else: bucket.append(k)

    return count
                        