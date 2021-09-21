

import numpy as np
from pandas import DataFrame as dF
from pandas import concat
from os import system
cls = lambda: system("clear")


Seq = [0, 15, 1, 14, 3, 12, 2, 13]

sLen = len(seq)

jin = ['0', '1', 'X', 'X']
kin = jin[::-1]

Seqbin = [[int(b) for b in bin(B)[2:].zfill(4)] for B in Seq]

jx = [[jin[Seqbin[n][c] * 2 + Seqbin[(n + 1) % sLen][c]] for c in range(4)] for n in range(sLen)]
kx = [[kin[Seqbin[n][c] * 2 + Seqbin[(n + 1) % sLen][c]] for c in range(4)] for n in range(sLen)]
ZZ = [[c + d for c, d in zip(a, b)] for a, b in zip(jx, kx)]
jkx = np.array([list("".join(a)) for a in ZZ])

Qn = dF(np.array([[str(n) for n in m] for m in Seqbin]), index = Seq, columns = ['Q3', 'Q2', 'Q1', 'Q0'])
jkCols = ''.join(['J' + str(n) + ' K' + str(n) + ' ' for n in range(3, -1, -1)]).split()

jkFFseq = dF(jkx, index=Seq, columns = jkCols)

Div = dF(np.array([['|']]*sLen), index=Seq, columns=['|'])

jkdF = concat([Qn, Div, jkFFseq], axis=1)

print('\n\n', jkdF, '\n\n')


