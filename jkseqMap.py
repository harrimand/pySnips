
from jkseq import *
from kmap import *
import qm

gcs = [n ^ n>>1 for n in range(16)]

# m = lambda S: [S[:4]]+[S[7:3:-1]]+[S[8:12]]+[S[15:11:-1]]
# Qseq = [[jkdF[[Qn]].loc[n].tolist()[0] for n in seq] for Qn in jkCols]

Qseq = [[jkdF.loc[n, Qn][0] for n in gcs] for Qn in jkCols]

KM = [karnaughMap(Q, 10) for Q in Qseq]

for S in KM: 
    S[2] = S[2].replace('C ', 'Q1')
    S[9] = S[9].replace('B ', 'Q2')
    S[11] = S[11].replace('A ', 'Q3')
    S[16] = S[16].replace('D ', 'Q0')

for i in range(0,7,2):
    print('\n\t', jkCols[i], ' '*40, jkCols[i+1])
    for J, K in zip(KM[i], KM[i+1]):
        print(J, K)

IMPS = [[seq[i] for i, n in enumerate(jkdF.loc[:, Q]) if n == '1'] for Q in jkCols]
DCimps = [[seq[i] for i, n in enumerate(jkdF.loc[:, Q]) if n == 'X'] for Q in jkCols]

i = 0 
for I, D in zip(IMPS, DCimps):
    print(jkCols[i])
    print('IT: ', I)
    print('DC: ', D)
    print(F'{jkCols[i]} = ', qm.tt2ssop(I, D)) 
    i += 1

print('\n\n')


'''

print('\n\n')

'''
KMAP = karnaughMap(k0seq, 10)
print('\n\n\tK0')
for K in KMAP:
    print(K)
print('\n\n')
'''

