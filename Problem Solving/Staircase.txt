def staircase(n):
    for i in range(n):
        j = n-(i+1)
        if j == 0:
            print("#"*(i+1))
        else:
            print(" "*(j-1), "#"*(i+1))