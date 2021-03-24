def timeInWords(h, m):
    keys = {
        0:"o' clock", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"quarter", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 21:"twenty one", 22:"twenty two", 23:"twenty three", 24:"twenty four", 25:"twenty five", 26:"twenty six", 27:"twenty seven", 28:"twenty eight", 29:"twenty nine", 30:"half"
    }
    
    if m == 0:
        return f"{keys[h]} {keys[m]}"
    if m <= 30:
        if m in (15, 30):
            return f"{keys[m]} past {keys[h]}"
        else:
            if m == 1:
                return f"{keys[m]} minute past {keys[h]}"
            else:
                return f"{keys[m]} minutes past {keys[h]}"
    else:
        m = 60 - m
        if m in (15, 30):
            return f"{keys[m]} to {keys[h+1]}"
        else:
            if m == 1:
                return f"{keys[m]} minute to {keys[h+1]}"
            else:
                return f"{keys[m]} minutes to {keys[h+1]}"