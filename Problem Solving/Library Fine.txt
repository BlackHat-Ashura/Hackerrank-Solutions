def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 - y2 > 0:
        return 10000
    elif y1 == y2 and m1 - m2 > 0:
	'''
	If y1 < y2 and m1 > m2 
	then fine should not be imposed.
	To ensure this y1 == y2 is checked.
	'''
        return (m1 - m2) * 500
    elif y1 == y2 and m1 == m2 and d1 - d2 > 0:
	'''
	If y1 < y2 or y1 == y2, m1 < m2 or m1 == m2 and d1 > d2
	then fine should not be imposed.
	To ensure this y1 == y2 and m1 == m2 is checked.
	'''
        return (d1 - d2) * 15
    else:
        return 0