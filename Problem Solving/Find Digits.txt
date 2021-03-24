def findDigits(n):
    count = 0
    n1 = n
    while n1:
        f = n1%10
        if f != 0 and n%f == 0:
            count += 1
        n1 = n1//10
    return count