def climbingLeaderboard(ranked: List[int], player: List[int]) -> List[int]:
    # this leaderboard doesn't increment the ranking on ties... so you could be #2 with four people tied for first
    leaderboard = list(sorted(set(ranked), reverse=True))
    output_list = []

    for score in player:
        low_idx = 0
        high_idx = len(leaderboard) - 1
        

        while low_idx <= high_idx:
            m = (high_idx + low_idx)//2

            if score == leaderboard[m]:
                low_idx = m
                # output_list.append(m + 1) 
                break
            elif score > leaderboard[m]:
                high_idx = m - 1
            elif score < leaderboard[m]:
                low_idx = m + 1
            
        output_list.append(low_idx + 1)

    return output_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()