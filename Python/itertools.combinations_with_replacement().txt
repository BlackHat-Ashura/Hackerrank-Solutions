import itertools

string, r = input().split()

for s in itertools.combinations_with_replacement(sorted(string), int(r)):
    print("".join(s))
