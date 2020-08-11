
from qm import *
import numpy as np

NOT = lambda M: [0 if(m) else 1 for m in M]
AND = lambda M, N: [m and n for m, n in zip(M, N)]
NAND = lambda M, N: [0 if(m and n) else 1 for m, n in zip(M, N)]
OR = lambda M, N: [m or n for m, n in zip(M, N)]
NOR = lambda M, N: [0 if(m or n) else 1 for m, n in zip(M, N)]
XOR = lambda M, N: [m ^ n for m, n in zip(M, N)]
XNOR = lambda M, N: [0 if(m ^ n) else 1 for m, n in zip(M, N)]

N = np.arange(16)
BN = np.array([[int(b) for b in bin(n)[2:].zfill(int(max(N)).bit_length())] for n in N])


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

print('NOT(B): '.ljust(14), NOT(B))
print('\n')

print('AND(B, C): '.ljust(14), AND(B, C))
print('\n')

print('NAND(B, C): '.ljust(14), NAND(B, C))
print('\n')

print('OR(B, C): '.ljust(14), OR(B, C))
print('\n')

print('NOR(B, C): '.ljust(14), NOR(B, C))
print('\n')

print('XOR(B, C): '.ljust(14), XOR(B, C))
print('\n')

print('XNOR(B, C): '.ljust(14), XNOR(B, C))
print('\n')

print("Q = A ^ B XOR C ^ D OR B ^ C")
print("Q = OR(XOR(AND(A, B), AND(C, D)), XOR(B, C))")
print("Q2 = OR(AND(C, XOR(A, D)), XOR(B, C))")
Q = np.array(OR(XOR(AND(A, B), AND(C, D)), XOR(B, C)))
Q2 = np.array(OR(AND(C, XOR(A, D)), XOR(B, C)))

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


