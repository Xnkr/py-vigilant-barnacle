def climbingLeaderboard(scores, alice):
    result = []
    for m in alice:
        prev_score = -1
        rank = 0
        found = False
        for n in scores:
            if prev_score == -1 or prev_score != n:
                rank +=1 
            prev_score = n
            if m >= n:
                result.append(rank)
                found = True
                break
        if not found:
            result.append(rank+1)