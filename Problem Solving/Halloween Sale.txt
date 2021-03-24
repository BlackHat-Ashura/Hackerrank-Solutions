def howManyGames(p, d, m, s):
    cost = 0
    i = 0
    while cost <= s:
        if p > m:
            cost += p
            p -= d
        else:
            p = m
            cost += p
        if cost > s:
            break
        i += 1
    return i