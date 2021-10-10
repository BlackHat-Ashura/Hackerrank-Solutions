import itertools

string, size = input().split()
list_ = list(itertools.permutations(string, int(size)))
permutation = []
for s in list_:
    permutation.append("".join(s))

permutation.sort()
print("\n".join(permutation))


##########################################################################

import itertools

string, size = input().split()
list_ = itertools.permutations(sorted(string), int(size))
for s in list_:
    print("".join(s))
