
from math import sqrt
import csv

def isprime(m):
    for n in range(3, int(sqrt(m))+1, 2):
        if m % n == 0:
            return False
    return True

def primeList(max):
    L = [2]
    for n in range(3, max, 2):
        if isprime(n):
            L.append(n)
    return L

def csvw(Primes):
    with open("Primes.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(Primes)

def binw(Primes):
    with open("binfile", 'w+b')as f:
        binary_format = bytearray(Pints)
        f.write(binary_format)

def primeaddends(N):
    if (N > 2) and (N % 2 == 0):
        adds = []
        m = 0
        while Pints[m] < (N / 2 + 1):
            if (N - Pints[m]) in Pints:
                adds.append((Pints[m], N - Pints[m]))
            m += 1
        return adds

def primeadds(N):
    pradds = {}
    for n in range(4, N, 2):
        a = primeaddends(n)
        if len(a) > 0:
            pradds[n] = a
    return pradds

MaxN = 400

Pints = primeList(MaxN)
Primes = [[str(P)] for P in Pints]
print(Pints)
# print(str(Pints[50]))
print("Length: ", len(Primes))

csvw(Primes)

pradds = primeadds(MaxN)
for k in pradds.keys():
    print(k, pradds[k])

# print(pradds)

