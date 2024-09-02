def solution(id_list, report, k):
    report_list = {id: [] for id in id_list}
    report_count = dict.fromkeys(id_list, 0)
    answer = dict.fromkeys(id_list, 0)
    
    for i in report:
        id, reported_id = i.split()
        if reported_id not in report_list[id]:
            report_list[id].append(reported_id)
            report_count[reported_id] += 1

    for key, value in report_count.items():
        for j_key, j_value in report_list.items():
            if value >= k and key in j_value:
                answer[j_key] += 1
            
    return list(answer.values())
