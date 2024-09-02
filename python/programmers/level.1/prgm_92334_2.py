def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_count = {x : 0 for x in id_list}

    for i in set(report):
        reported_id = i.split()[1]
        report_count[reported_id] += 1

    for i in set(report):
        id, reported_id = i.split()
        if report_count[reported_id] >= k:
            answer[id_list.index(id)] += 1

    return answer