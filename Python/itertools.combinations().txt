import itertools

word_str, C = input().split()
word_list = []

for i in range(1, int(C)+1):
    combinations = itertools.combinations(sorted(word_str), i)
    word_list.extend(list(combinations))

for s in word_list:
    print("".join(s))


############################################################################

import itertools

word_str, C = input().split()

for i in range(1, int(C)+1):
    for s in itertools.combinations(sorted(word_str), i):
        print("".join(s))
