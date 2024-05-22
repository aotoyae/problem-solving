def solution(polynomial):
    new_arr = polynomial.split(" + ")
    num_x = 0
    num = 0

    for item in new_arr:
        if "x" in item:
            x_arr = item.split("x")

            if x_arr[0] == "": num_x += 1
            else: num_x += int(x_arr[0])
        else:
            num += int(item)

    if num_x != 0 and num != 0:
        return f"x + {num}" if num_x == 1 else f"{num_x}x + {num}"
    if num_x != 0 and num == 0:
        return "x" if num_x == 1 else f"{num_x}x"
    if num_x == 0 and num != 0:
        return f"{num}"
    
    return "0"