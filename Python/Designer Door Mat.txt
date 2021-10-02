n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])

dot_pipe_dot = 1

for i in range(n//2):
    dash = (m - dot_pipe_dot*3)//6
    print("---"*dash + ".|."*dot_pipe_dot + "---"*dash)
    dot_pipe_dot += 2

welcome = "WELCOME"
central_dash = (m - len(welcome))//2
print("-"*central_dash + welcome + "-"*central_dash)

dot_pipe_dot -= 2

for i in range(n//2):
    dash = (m - dot_pipe_dot*3)//6
    print("---"*dash + ".|."*dot_pipe_dot + "---"*dash)
    dot_pipe_dot -= 2


##########################################################################

N,M = map(int,input().split())

for i in range(1, N, 2):
    print((str('.|.')*i ).center(M, '-'))

print(str('WELCOME').center(M, '-'))

for i in range(N-2, -1, -2): 
    print((str('.|.')*i ).center(M, '-'))
