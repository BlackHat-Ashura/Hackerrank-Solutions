def dayOfProgrammer(year):
    if year<=1917:
        if year%4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year>=1919:
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"        
    else:
        """
        12.09.1918 + 14 days = 26.09.1918
        """
        return "26.09.1918"