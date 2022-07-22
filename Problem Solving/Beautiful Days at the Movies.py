def beautifulDays(i, j, k):
    count = 0
    def revnum(num):
        rev = 0
        while num:
            rev = rev*10 + num%10
            num = num//10
        return rev
    for day in range(i, j+1):
        revday = revnum(day)
        diff = day - revday
        if diff%k == 0.:
            count += 1
    return count