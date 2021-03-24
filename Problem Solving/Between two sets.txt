def getTotalX(a, b):
    def HCF(x, y):
        if y==0:
            return x
        return HCF(y, x%y)
    def LCM(x, y):
        return x*y//HCF(x, y)
    
    l = a[0]
    for i in range(len(a)-1):
        l = LCM(l, a[i+1])
    
    h = b[0]
    for i in range(len(b)-1):
        h = HCF(h, b[i+1])
    
    s = 0
    for i in range(l, h+1, l):
        if h%i == 0:
            s += 1
    
    return s