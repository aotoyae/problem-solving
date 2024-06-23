def solution(sizes):
    width=[]
    height=[]

    for i in sizes:
        sorted_size = sorted(i)
        width.append(sorted_size[0])
        height.append(sorted_size[1])

    return max(width) * max(height)