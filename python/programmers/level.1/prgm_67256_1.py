def solution(numbers,hand):
    pad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           "*": [3, 0], 0: [3, 1], "#": [3, 2]}
    
    left_arr = [1, 4, 7]
    right_arr = [3, 6, 9]
    left = pad["*"]
    right = pad["#"]

    result = ""

    for i in numbers:
        if i in left_arr:
            result += "L"
            left = pad[i]
        elif i in right_arr:
            result += "R"
            right = pad[i]
        else:
            left_dis = abs(left[0] - pad[i][0]) + abs(left[1] - pad[i][1])
            right_dis = abs(right[0] - pad[i][0]) + abs(right[1] - pad[i][1])

            if left_dis < right_dis:
                result += "L"
                left = pad[i]
            elif left_dis > right_dis:
                result += "R"
                right = pad[i]
            else:
                if hand == "left":
                    result += "L"
                    left = pad[i]
                else:
                    result += "R"
                    right = pad[i]
    
    return result
