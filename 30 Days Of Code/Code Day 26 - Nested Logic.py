def fine(returned, due):
    d1 = returned[0]
    d2 = due[0]
    m1 = returned[1]
    m2 = due[1]
    y1 = returned[2]
    y2 = due[2]
    if y1>y2:
        return 10000
    elif y1 == y2 and m1>m2:
        return (m1 - m2) * 500
    elif y1 == y2 and m1 == m2 and d1>d2:
        return (d1 - d2) * 15
    else:
        return 0

if __name__ == '__main__':
    returned = input().split()
    r = list(map(int, returned))
    due = input().split()
    d = list(map(int, due))
    print(fine(r, d))