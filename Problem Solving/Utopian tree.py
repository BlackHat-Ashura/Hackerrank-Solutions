def utopianTree(n):
    if n == 0:
        return 1
    else:
        height = 1
        for i in range(1,n+1):
            if i%2 == 0:
                height += 1
            else:
                height = height*2    
    return height