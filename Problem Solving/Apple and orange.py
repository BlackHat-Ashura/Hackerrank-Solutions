def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_c = 0
    oranges_c = 0
    for i in range(len(apples)):
        apples[i] += a
        if apples[i] in range(s, t+1):
            apples_c += 1
    for i in range(len(oranges)):
        oranges[i] += b
        if oranges[i] in range(s, t+1):
            oranges_c += 1
    print(apples_c)
    print(oranges_c)