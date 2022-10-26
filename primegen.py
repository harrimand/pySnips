#!/usr/bin/env python3

from math import sqrt
import csv
from os import system

cls = lambda: system("clear")

def isprime(m):
    for n in range(3, int(sqrt(m))+1, 2):
        if m % n == 0:
            return False
    return True

def primeList(mx):
    L = [2]
    for n in range(3, mx, 2):
        if isprime(n):
            L.append(n)
    return L

def primeRange(begin, end):
    begin = begin + ((begin + 1) % 2)
    L = []
    for n in range(begin, end + 1, 2):
        if isprime(n):
            L.append(n)
    return L

def primeCount(count):
    cnt = 1
    L = [2]
    p = 3
    while cnt < count:
        if isprime(p):
            L.append(p)
            cnt += 1
        p += 2
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

diffs = lambda pc: [pc[i+1]-n for i, n in enumerate(pc[:-1])]
ndiffs = lambda d: {n: d.count(n) for n in set(d)}


def primeHelp():
    helpstr = "\n\
        isprime(N):  Return true if N is prime.  False otherwise\n\
        primeList(mx): Return all prime numbers up to mx\n\
        primeRange(begin, end): Return list of primes between begin and end inclusive\n\
        primeCount(N): Return list containing quantity N prime numbers\n\
        csvw(Primes): Write Primes list to CSV file\n\
        binw(Primes): Write Primes list to BIN file\n\
        primeaddends(N): Helper Function to be called by primeadds(N)\n\
        primeadds(N): Return list of pairs of prime numbers that add up\n\
             to all even numbers > 2 & < N\n\
        consecs(Primes): Return list of tuples of prime numbers differing by 2\n\
        diffs(Primes): Return list of differences between prime numbers in list\n\
        ndiffs(diffs(Primes)): Return dictionary with keys = diffs, values = counts\n"
    print("\n", helpstr)

consecs = lambda p: [(c, p[i+1]) for i, c in enumerate(p[:-1]) if c == (p[i + 1] - 2)]

if __name__ == "__main__":
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

