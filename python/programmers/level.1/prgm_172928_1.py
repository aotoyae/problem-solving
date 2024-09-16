def solution(park, routes):
    x, y = 0, 0
    w, h = len(park[0]), len(park)
    op = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x, y = i, j
                break
    
    for route in routes:
        way, num = route.split(" ")
        cur_x, cur_y = x, y

        for i in range(int(num)):
            num_x = x + op[way][0]
            num_y = y + op[way][1]

            if 0 <= num_x <= h - 1 and 0 <= num_y <= w - 1 and (park[num_x][num_y] != 'X'):
                x, y = num_x, num_y
            else:
                x, y = cur_x, cur_y
                break
    
    return [x, y]