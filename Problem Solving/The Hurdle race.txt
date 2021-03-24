def hurdleRace(k, height):
    max = 0
    for i in height:
        if max < i:
            max = i
    if k < max:
        return max - k
    else:
        return 0