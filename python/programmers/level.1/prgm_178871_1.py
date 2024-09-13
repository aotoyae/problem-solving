def solution(players, callings):
    player_dic = {player: idx for idx, player in enumerate(players)}

    for name in callings:
        idx = player_dic[name] # index 대신 dic 을 활용
        players[idx], players[idx - 1]  = players[idx - 1], name

        player_dic[players[idx]] = idx
        player_dic[players[idx - 1]] = idx - 1

    return players