def alt(ar):
    l = len(ar)
    ev = ""
    od = ""
    for i in range(0, l):
        if i%2 == 0:
            ev += ar[i]
        else:
            od += ar[i]
    return ev + " " + od

if __name__ == '__main__':
    n = int(input())
    res = []
    for i in range(n):
        s = input().rstrip()
        print(alt(s))