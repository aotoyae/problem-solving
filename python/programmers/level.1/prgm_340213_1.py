def solution(video_len, pos, op_start, op_end, commands):
    video_len_t = int(video_len.replace(":", ""))
    pos_t = int(pos.replace(":", ""))
    op_start_t = int(op_start.replace(":", ""))
    op_end_t = int(op_end.replace(":", ""))

    if op_start_t <= pos_t <= op_end_t:
        pos_t = op_end_t

    for command in commands:
        if command == "next":
            if pos_t % 100 > 50:
                pos_t += 50
            else:
                pos_t += 10

            if op_start_t <= pos_t <= op_end_t:
                pos_t = op_end_t
            if pos_t > video_len_t:
                pos_t = video_len_t
        else:
            if pos_t < 10:
                pos_t = 0
            elif pos_t % 100 < 10:
                pos_t -= 50
            else:
                pos_t -= 10

            if op_start_t <= pos_t <= op_end_t:
                pos_t = op_end_t

    minutes = str(pos_t // 100).zfill(2)
    seconds = str(pos_t % 100).zfill(2)

    return f"{minutes}:{seconds}"