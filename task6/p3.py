def create_leaderboard(ranked,players):
    leaderboard = []
    for i in range(players):
        if ranked[i] == ranked[i-1]:
            continue
        leaderboard.append(ranked[i])
        # print(leaderboard)
    return leaderboard


def get_rank(leaderboard, game_score):
    currentboard = leaderboard.copy()
    currentboard.append(game_score)
    currentboard.sort(reverse = True)
    # print(currentboard)
    score = currentboard.index(game_score) + 1
    currentboard.clear()
    return score


def main():
    players = int(input())
    ranked = list(map(int, input().split()))
    leaderboard = create_leaderboard(ranked,players)
    games = int(input())
    player_scores = list(map(int, input().split()))
        
    current_rank = []
    for i in range(games):
        game_score = player_scores[i]
        # print(game_score)
        current_rank.append(get_rank(leaderboard, game_score))
    
    for i in range(games):
        print(current_rank[i])
main()