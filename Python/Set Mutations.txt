N = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    # cmd = input().split()[0]
    # set_2 = set(map(int, input().split()))
    # eval(f"A.{cmd}(set_2)")
    eval("A.{0}({1})".format(input().split()[0], set(map(int, input().split()))))

print(sum(A))
