from qm import *
import numpy as np
# from os import sys


NOT = lambda M: [0 if(m) else 1 for m in M]
AND = lambda M, N: [m and n for m, n in zip(M, N)]
NAND = lambda M, N: [0 if(m and n) else 1 for m, n in zip(M, N)]
OR = lambda M, N: [m or n for m, n in zip(M, N)]
NOR = lambda M, N: [0 if(m or n) else 1 for m, n in zip(M, N)]
XOR = lambda M, N: [m ^ n for m, n in zip(M, N)]
XNOR = lambda M, N: [0 if(m ^ n) else 1 for m, n in zip(M, N)]

bit = lambda b, numbits: [n//(2**b)%2 for n in range(2**numbits)]

ttIn = lambda nb:[[int(b) for b in np.array(list(bin(n)[2:].zfill(nb)))] for n in np.arange(2**nb)]
colImps = lambda t, c: [int(n) for n in np.where(t[:,c] == 1)[0]]
imps = lambda tc: list([n for n in np.where(np.array(tc) == 1)][0])
npcolb = lambda t, c: [b for b in t[:,c]]
colb = lambda t, c: [t[n][c] for n in range(2**(len(t[0])))]
npArr2List = lambda npList: [[int(t) for t in s] for s in npList]
addCol = lambda table, newcol: [list(B) for B in np.hstack((table, [[n] for n in newcol]))]

# addCol = lambda table, newcol: np.hstack((table, [[n] for n in newcol]))


'''
A = bit(3, 4) # bit 3 of 4 bits
B = bit(2, 4) # bit 2 of 4 bits
C = bit(1, 4) # bit 1 of 4 bits
D = bit(0, 4) # bit 0 of 4 bits


def table(nbits):
    N = np.arange(2**nbits)
    BN = np.array([[int(b) for b in bin(n)[2:].zfill(int(max(N)).bit_length())] for n in N])
    return BN

BN = table(4)
print(BN)

A = BN[:,0]
B = BN[:,1]
C = BN[:,2]
D = BN[:,3]

print('\n\n')

print('\n\nA: ', A)
print('\n\nB: ', B)
print('\n\nC: ', C)
print('\n\nD: ', D)

print('\n\n')



# Qssop:  !B!C + A!C + BC + CD

print("Q = A ^ B XOR C ^ D OR B ^ C")
print("Q = OR(XOR(AND(A, B), AND(C, D)), XOR(B, C))")
print("Q2 = OR(AND(C, XOR(A, D)), XOR(B, C))")
Q = np.array(OR(XOR(AND(A, B), AND(C, D)), XNOR(B, C)))
Q2 = np.array(OR(OR(AND(A, NOT(C)), XNOR(B, C)), AND(C, D)))

print('Q: ', Q)

Qi = np.where(Q == 1)
Qi2 = np.where(Q2 == 1)
print('\n')

Qimps = [int(n) for n in Qi[0]]
Qimps2 = [int(n) for n in Qi2[0]]

Vars = [chr(n) for n in range(65, 69)]
print('Vars: ', Vars)

dc = []
Qssop = tt2ssop(Qimps, dc)
Qssop2 = tt2ssop(Qimps2, dc)

print('\n')
print('Qssop: ', Qssop)
print('Qssop2: ', Qssop2)

print('\n\n')
'''


