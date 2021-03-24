def repeatedString(s, n):
    l = len(s)
    a = s.count('a')
    if n%l == 0:
        return (n//l) * a
    else:
        rem = n%l
        return (n//l) * a + s[:rem].count('a')