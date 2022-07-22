def kaprekarNumbers(p, q):
    def kaprekar(n):
        sq = str(n**2)
        first = sq[:len(sq)//2]
        second = sq[len(sq)//2:]
        if not second:
            second = 0
        if int(first) + int(second) == n:
            return True
    out = []
    for i in range(p, q+1):
        if kaprekar(i) == True:
            out.append(i)
    if out:
        for i in out:
            print(i, end=" ")
    else:
        print("INVALID RANGE")