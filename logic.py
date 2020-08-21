from qm import *
import numpy as np
# from os import sys


NOT = lambda M: [0 if(m) else 1 for m in M]
# AND = lambda M, N: [m and n for m, n in zip(M, N)]
# NAND = lambda M, N: [0 if(m and n) else 1 for m, n in zip(M, N)]
# OR = lambda M, N: [m or n for m, n in zip(M, N)]
# NOR = lambda M, N: [0 if(m or n) else 1 for m, n in zip(M, N)]
# XOR = lambda M, N: [m ^ n for m, n in zip(M, N)]
# XNOR = lambda M, N: [0 if(m ^ n) else 1 for m, n in zip(M, N)]

bit = lambda b, numbits: [n//(2**b)%2 for n in range(2**numbits)]

ttIn = lambda nb:[[int(b) for b in np.array(list(bin(n)[2:].zfill(nb)))] for n in np.arange(2**nb)]
colImps = lambda t, c: [int(n) for n in np.where(t[:,c] == 1)[0]]
imps = lambda tc: list([n for n in np.where(np.array(tc) == 1)][0])
npcolb = lambda t, c: [b for b in t[:,c]]
colb = lambda t, c: [t[n][c] for n in range(2**(len(t[0])))]
npArr2List = lambda npList: [[int(t) for t in s] for s in npList]
addCol = lambda table, newcol: [list(B) for B in np.hstack((table, [[n] for n in newcol]))]
cols = lambda tt: list(map(list, zip(*tt)))
# addCol = lambda table, newcol: np.hstack((table, [[n] for n in newcol]))



def AND(*argv):
    """a and b and c and d"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = Q and a
        QList.append(int(Q))
    return QList

# M = list(map(list, zip(a, b, c)))

def NotAND(*argv):
    """not(a and b and c)"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = Q and a
        QList.append(int(not Q)) 
    return QList

def NAND(*argv):
    """not(not(a and b) and c)"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = not(Q and a)
        QList.append(int(Q))
    return QList

def OR(*argv):
    """a or b or c or d"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = Q or a
        QList.append(int(Q))
    return QList

# M = list(map(list, zip(a, b, c)))

def NotOR(*argv):
    """not(a or b or c or d)"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = Q or a
        QList.append(int(not Q))
    return QList

def NOR(*argv):
    """not(not(not(a or b) or c) or d)"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = not(Q or a)
        QList.append(int(Q))
    return QList

def XOR(*argv):
    """a xor b xor c xor d"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = Q ^ a
        QList.append(int(Q))
    return QList

def XNOR(*argv):
    """not(not(not(a xor b) xor c) xor d)"""
    QList = []
    for A in list(map(list, zip(*argv))):
        Q = A[0]
        for a in A[1:]:
            Q = not(Q ^ a)
        QList.append(int(Q))
    return QList

