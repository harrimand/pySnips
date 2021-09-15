
import numpy as np
from pandas import DataFrame as dF

from os import system
cls = lambda: system("clear")

# A = [['a', 'c', 'e'], ['g', 'i', 'k'], ['m', 'o', 'q'], ['s', 'u', 'w']]
# B = [['b', 'd', 'f'], ['h', 'j', 'l'], ['n', 'p', 'r'], ['t', 'v', 'x']]

alpha = [chr(n) for n in range(97, 121)]

A = np.reshape(alpha[::2], (3, 4))
B = np.reshape(alpha[1::2], (3, 4))

Z = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]

ABC = np.array([list("".join(a)) for a in Z])

print('\n\nA = \n', A)
print('\n\nB = \n', B)
print('\n\nZ = \n', Z)
print('\n\nAB = \n', ABC, '\n\n')

print('-'*80, '\n\n')

jKCols = ['J3', 'K3', 'J2', 'K2', 'J1', 'K1', 'J0', 'K0']


ABCdF = dF(ABC, index=['0', '1', '3'], columns = jkCols)

print(ABCdF)
#-----------------------------------------------------------------------------
'''
import numpy as np


from pandas import DataFrame as dF
from pandas import concat


from os import system
cls = lambda: system("cls")

seq = [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
jin = ['0', '1', 'X', 'X']
kin = jin[::-1]

seqbin = [[int(b) for b in bin(B)[2:].zfill(4)] for B in seq]

seqbinN = np.array(seqbin)

# print(seqbinN)

jx = [[jin[seqbin[n][c] * 2 + seqbin[16 % (n + 1)][c]] for c in range(4)] for n in range(16)]

kx = [[kin[seqbin[n][c] * 2 + seqbin[16 % (n + 1)][c]] for c in range(4)] for n in range(16)]

Z = [[c + d for c, d in zip(a, b)] for a, b in zip(jx, kx)]

jkx = np.array([list("".join(a)) for a in Z])

print('\n\n', jkx)

Qn = dF(np.array([[str(n) for n in m] for m in seqbin]), index = seq, columns = ['Q3', 'Q2', 'Q1', 'Q0'])

jkCols = ''.join(['J' + str(n) + ' K' + str(n) + ' ' for n in range(3, -1, -1)]).split()

jkFFseq = dF(jkx, index=seq, columns = jkCols)

print('\n\n')
print(jkFFseq)

jkdF = concat([Qn, jkFFseq], axis=1)

print('\n\n', jkdF, '\n\n')

'''






