# O(n) time complexity since we traverse the games in the competition once; reading & writing to dict is constant time
# O(k) size complexity to store dictionary of scores one for each team (which is the inverse of n choose k of games in competition)
# the sring length is maxed at 30 so it is 30k = O(k)
def tournamentWinner(competitions, results):
    scores = {}
    leader_score = ["", 0]
    for idx, game in enumerate(competitions):
        if results[idx] == 0:
            winner = game[1]
        else:
            winner = game[0]
        if winner in scores.keys():
            scores[winner] += 3
        else:
            scores[winner] = 3
        if scores[winner] > leader_score[1]:
            leader_score = [winner, scores[winner]]

    return leader_score[0]