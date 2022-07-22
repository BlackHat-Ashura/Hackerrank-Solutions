def jumpingOnClouds(c, k):
    i = k%n
    energy = 99
    while i:
        if c[i] == 1:
            energy -= 2
        i = (i + k)%n
        energy -= 1
    if c[i] == 1:
            energy -= 2
    return energy

'''Improved solution'''

def jumpingOnClouds(c, k):
    i = 0
    energy = 100
    while True:
        energy -= 1 + 2*c[i]
        i = (i + k) % n
        if i == 0:
            break
    return energy