
def climbingLeaderboard(ranked, player):
    result = []
    
    ranked = sorted(list(set(ranked)), reverse = True)
    player = sorted(player, reverse = True)
    
    i, j = 0, 0
    while i < len(player):
        while j < len(ranked):
            if player[i] >= ranked[j]:
                break
            j += 1
        result.append(j+1)
        i += 1
        
    return result[::-1]


print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))
