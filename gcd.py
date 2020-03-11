#!/usr/bin/env python3
# Find Prime factors and Greatest Common Factor for multiple inputs.
# python gcd.py 1248913463875 50641529357890625 2036322180011590625
# ./gcd.py 593890605 112120605 

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

def printExpStr(n, PF):
# Formatting list to display exponential string
    UF = set(PF)    # Unique set of factors
    CF = []         # List for exponential notation
    for U in UF: 
        if PF.count(U) > 1:
            CF.append(str(U) + '^' + str(PF.count(U)))
        else:
            CF.append(str(U))

    print('\n\t', n, ' = ', ' * '.join(CF), '\n')

#-------------------------------------------------------------------

# Getting user input from command line

F = []
if len(sys.argv) > 1:
    n = sys.argv[1:]
    for N in n:
        F.append(prime_factors(int(N)))
else:
    print('\nNo User Input!  Using test number.')
    n = 1366776851540808708000000
    F.append(prime_factors(int(n)))

prWidth = max([len(str(fact)) for fact in n]) + 2 

print('\n')
for pf, arg in zip(F, n): 
    print(str(arg).rjust(prWidth), 'factors:', pf) 
    printExpStr(arg, pf) 
    print('\n')

Fs = set(F[0])
# Fs = list(set(F[0])).sort()
# GC = [s ** min(F[0].count(s), F[1].count(s)) for s in Fs if min(F[0].count(s), F[1].count(s))]

GC = [s ** min([F[Fs].count(s) for Fs in range(len(F))]) for s in Fs if min([F[Fs].count(s) for Fs in range(len(F))])]

GCF = 1 
for n in GC: 
    GCF *= n

print('Common Factors: ', GC) 
print('\nGreatest Common Factor: ', GCF, '\n\n')
