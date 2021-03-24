def timeConversion(s):
    if s[-2:]=="PM":
        time = int(s.split(':')[0])
        if time!=12:
            time += 12
        return str(time)+s[2:-2]
    if s[-2:]=="AM":
        time = int(s.split(':')[0])
        if time==12:
            return "00"+s[2:-2]
        return s[:-2]
