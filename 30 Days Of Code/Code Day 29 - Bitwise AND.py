def bitwiseAnd(N, K):
    max_ = 0
    a = N - 1
    while(a > 0):
        for b in range(a+1, N+1):
            test = a & b
            if test < K and test > max_:
                max_ = test
                if max_ + 1 == K:
                    return max_
        a -= 1
    return max_
