from jkseq import *
from kmap import *

gcs = [n ^ n>>1 for n in range(16)]

m = lambda S: [S[:4]]+[S[7:3:-1]]+[S[8:12]]+[S[15:11:-1]]

# Qseq = [[jkdF[[Qn]].loc[n].tolist()[0] for n in seq] for Qn in jkCols]

Qseq = [[jkdF.loc[n, Qn][0] for n in gcs] for Qn in jkCols]

KM = [karnaughMap(Q, 10) for Q in Qseq]

for i in range(0,7,2):
    print('\n\t', jkCols[i], ' '*40, jkCols[i+1])
    for J, K in zip(KM[i], KM[i+1]):
        print(J, K)

'''
for i, KK in enumerate(KM):
    print('\n\t', jkCols[i])
    for K in KK:
        print(K)
'''

print('\n\n')

'''
KMAP = karnaughMap(k0seq, 10)
print('\n\n\tK0')
for K in KMAP:
    print(K)
print('\n\n')
'''

