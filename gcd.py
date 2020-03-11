
from os import sys

#-------------------------------------------------------------------
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

#-------------------------------------------------------------------
# Getting user input from command line

F = []
if len(sys.argv) > 1:
    for n in sys.argv[1:]:
        F.append(prime_factors(int(n)))
else:
    print('\nNo User Input!  Using test number.')
    n = 1366776851540808708000000
    F.append(prime_factors(int(n)))

print('\n')
for n, pf in enumerate(F):
    print(sys.argv[n + 1], 'factors:', pf)

Fs = set(F[0])
# GC = [s ** min(F[0].count(s), F[1].count(s)) for s in Fs if min(F[0].count(s), F[1].count(s))]

# GC = [s ** min([F[Facts].count(s) for Facts in range(len(F))]) for s in Fs if min(F[0].count(s), F[1].count(s))]
GC = [s ** min([F[Facts].count(s) for Facts in range(len(F))]) for s in Fs if min([F[Facts].count(s) for Facts in range(len(F))])]

print('GC: ', GC)

GCF = 1
for n in GC:
    GCF *= n

print('\nGCF: ', GCF, '\n\n')


