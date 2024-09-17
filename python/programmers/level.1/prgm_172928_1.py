def solution(park, routes):
    x, y = 0, 0
    w, h = len(park[0]), len(park)
    op = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for i in range(h): # 시작 지점 찾기
        for j in range(w):
            if park[i][j] == "S":
                x, y = i, j
                break
    
    for route in routes:
        way, num = route.split(" ") # 방향, 거리
        cur_x, cur_y = x, y # 현 위치

        for i in range(int(num)):
            num_x = x + op[way][0] # 한 칸씩 이동한 값
            num_y = y + op[way][1]

            if 0 <= num_x < h and 0 <= num_y < w and (park[num_x][num_y] != 'X'):
                x, y = num_x, num_y
            else: # 이동하다가 조건에 맞지 않으면 원상복귀
                x, y = cur_x, cur_y
                break
    
    return [x, y]