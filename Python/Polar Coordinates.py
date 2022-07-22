import cmath

z = input()
phi = cmath.phase(complex(z))
r = abs(complex(z))

print(r)
print(phi)
