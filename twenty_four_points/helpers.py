
def get_ranking_string(players):
    message = "Current Ranking:\n"
    for i in range(len(players)):
        message += f"{i + 1}. {players[i][0]}\t{players[i][1]}\n"
    return message
