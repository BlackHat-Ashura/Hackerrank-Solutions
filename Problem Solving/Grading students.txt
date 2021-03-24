def gradingStudents(grades):
    result = []
    for i in grades:
        if i%5 > 2 and i-i%5+5 >= 40:
            result.append(i-i%5+5)
        else:
            result.append(i)
    return result