def acmTeam(topic):
    n = len(topic)
    max_total = 0
    count = 0
    for i in range(n):
        first = topic[i]
        for j in range(i+1, n):
            second = topic[j]
            sub = 0
            for x, y in zip(first, second):
                if x=='1' or y=='1':
                    sub += 1
            if sub > max_total:
                max_total = sub
                count = 1
            elif sub == max_total:
                count += 1
    return [max_total, count]