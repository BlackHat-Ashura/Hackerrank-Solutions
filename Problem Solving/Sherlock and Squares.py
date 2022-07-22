def squares(a, b):
    '''
    The number of perfect roots lies within the range
    of the root of upper and lower bounds.
    Eg:- 1, 4, 9, 16, 25, 36
	 if a = 8, b = 37
	 2 < root(a) < 3 --> Lower bound of roots (A = 3)
	 6 < root(b) < 7 --> Upper bound of roots (B = 6)
	 Therefore any number^2 between A and B lies within a and b.
    '''
    if a**0.5 > int(a**0.5):
        a = int(a**0.5) + 1
    else:
        a = int(a**0.5)
    b = int(b**0.5)
    return b - a + 1