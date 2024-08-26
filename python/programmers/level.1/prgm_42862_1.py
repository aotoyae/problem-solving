def solution(n, lost, reserve):
    lost_list = sorted([num for num in lost if num not in reserve])
    reserve_list = sorted([num for num in reserve if num not in lost])

    for num in reserve_list:
        if num - 1 in lost_list:
            lost_list.remove(num - 1)
        elif num + 1 in lost_list:
            lost_list.remove(num + 1)
    
    return n - len(lost_list)