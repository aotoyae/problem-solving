def solution(keymap, targets):
    dic = {}
    answer = []

    for key in keymap:
        for idx, val in enumerate(key):
            if val not in dic or dic[val] > idx + 1:
                dic[val] = idx + 1
    
    for target in targets:
        count = 0

        for word in target:
            if word in dic: count += dic[word]
            else:
                count = -1
                break

        answer.append(count)    
  
    return answer
            