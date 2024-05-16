def solution(common):
    gap = []

    for i in range(2):
        gap.append(common[i+1] - common[i])

    if gap[0] == gap[1]:
        return common[-1] + gap[0]
    else:
        return common[-1] * (gap[1] / gap[0])