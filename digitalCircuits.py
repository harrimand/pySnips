#!/usr/env/bin python3

import numpy as np
import pandas as pd

from os import system
cls = lambda: system("cls")

Btxt = [bin(n)[2:].zfill(4) for n in range(16)]
bints = [[int(s[n]) for n in range(4)] for s in Btxt]
bn = np.array(bints)
# A, B, C, D = bn[:,0], bn[:,1], bn[:,2], bn[:,3]

ops = ['As', 'Ap', 'Os', 'Op', 'Xs', 'Xp', 'NAs', 'NAp', 'NOs', 'NOp']

Funs = {'As': '(A * (B * (C * D)))',
        'Ap': '(A * B) * (C * D)',
        'Os': '(A + (B + (C + D)))',
        'Op': '(A + B) + (C + D)',
        'Xs': '(A ^ (B ^ (C ^ D)))',
        'Xp': '(A ^ B) ^ (C ^ D)',
        'NAs': '!(A * !(B * !(C * D))',
        'NAp': '!(!(A * B) * !(C * D))',
        'NOs': '!(A + !(B + !(C + D))',
        'NOp': '!(!(A + B) + !(C + D))'}
 
def showFuns():
    for F in Funs:
        print(F"\t {F} = {Funs[F]}")



F = {'A': A, 'B': B, 'C': C, 'D': D}


F['As'] = (A & (B & (C & D)))
F['Ap'] = (A & B) & (C & D)
F['Os'] = (A | (B | (C | D)))
F['Op'] = (A | B) | (C | D)
F['Xs'] = (A ^ (B ^ (C ^ D)))
F['Xp'] = (A ^ B) ^ (C ^ D)

for d in ops[-4:]:
    F[d] = []


for n in range(16):
    A, B, C, D = bn[n,0], bn[n,1], bn[n,2], bn[n,3]
    F['NAs'] = np.hstack((F['NAs'], np.array(not(A & (not(B & (not(C & D))))))))
    F['NAp'] = np.hstack((F['NAp'], np.array(not(not(A & B) & (not(C & D))))))
    F['NOs'] = np.hstack((F['NOs'], np.array(not(A | (not(B | (not(C | D))))))))
    F['NOp'] = np.hstack((F['NOp'], np.array(not(not(A | B) | (not(C | D))))))

TT = pd.DataFrame(F, dtype='int')

showFuns()


