N = int(input())
S = set(map(int, input().split()))

for _ in range(int(input())):
    func = input().split()
    eval("S.{0}({1})".format(*func + [' ']))

print(sum(S))
