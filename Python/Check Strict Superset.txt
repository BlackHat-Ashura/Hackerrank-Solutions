A = set(map(int, input().split()))
flag = True
for _ in range(int(input())):
    B = set(map(int, input().split()))
    if not (flag:=A.issuperset(B)):
        break

print(flag)
