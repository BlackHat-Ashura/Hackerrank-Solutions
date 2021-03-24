def breakingRecords(scores):
    high = [scores[0]]
    inc = 0
    low = [scores[0]]
    dec = 0
    for i in range(1, len(scores)):
        if scores[i]>high[i-1]:
            high.append(scores[i])
            inc += 1
        else:
            high.append(high[i-1])
        
        if scores[i]<low[i-1]:
            low.append(scores[i])
            dec += 1
        else:
            low.append(low[i-1])
    return inc, dec