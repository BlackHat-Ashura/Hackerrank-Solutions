def chocolateFeast(n, c, m):
    bars = n // c
    wrappers = bars
    while wrappers >= m:
        new_wrappers = wrappers//m
        bars += new_wrappers
        wrappers = wrappers%m + new_wrappers
    return bars