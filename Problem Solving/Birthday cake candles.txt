def birthdayCakeCandles(candles):
    maxnum = max(candles)
    c = 0
    for val in candles:
        if val == maxnum:
            c += 1
    return c