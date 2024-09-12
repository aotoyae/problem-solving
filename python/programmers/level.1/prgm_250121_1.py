def solution(data, ext, val_ext, sort_by):
    idx = { 'code': 0, 'date': 1, 'maximum': 2, 'remain': 3 }
    lst = []

    for item in data:
        if item[idx[ext]] < val_ext: lst.append(item)
    
    lst.sort(key=lambda x: x[idx[sort_by]])

    return lst