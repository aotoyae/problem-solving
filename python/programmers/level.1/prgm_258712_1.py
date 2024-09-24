def solution(friends, gifts):
    answer = 0
    gift_dic={k: {j: 0 for j in friends if j != k} for k in friends}
    gives = {k: 0 for k in friends}
    gets = {k: 0 for k in friends}

    for gift in gifts:
        send, target = gift.split()
        gift_dic[send][target] += 1
        gives[send] += 1
        gets[target] += 1

    for k in gift_dic.keys():
        count = 0

        for kk in gift_dic[k].keys():
            if gift_dic[k][kk] > gift_dic[kk][k]:
                count += 1
            elif gift_dic[k][kk] == gift_dic[kk][k]:
                if gives[k] - gets[k] > gives[kk] - gets[kk]:
                    count += 1
        answer = max(answer, count)

    return answer