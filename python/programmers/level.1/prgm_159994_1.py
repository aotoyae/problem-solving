def solution(cards1, cards2, goal):
    j = 0
    k = 0

    for word in goal:
        if len(cards1) > j and word == cards1[j]: j += 1
        elif  len(cards2) > k and word == cards2[k]: k += 1
        else: return "No"

    return "Yes"