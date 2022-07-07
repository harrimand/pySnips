
import numpy as np
import pandas as pd

from os import system
cls = lambda: system("clear")

Btxt = [bin(n)[2:].zfill(4) for n in range(16)]
bints = [[int(s[n]) for n in range(4)] for s in Btxt]
bn = np.array(bints)
A, B, C, D = bn[:,0], bn[:,1], bn[:,2], bn[:,3]

ops = ['As', 'Ap', 'Os', 'Op', 'Xs', 'Xp', 'NAs', 'NAp', 'NOs', 'NOp']

F = {'As': (A & (B & (C & D)))}
F['Ap'] = (A & B) & (C & D)
F['Os'] = (A | (B | (C | D)))
F['Op'] = (A | B) | (C | D)
F['Xs'] = (A ^ (B ^ (C ^ D)))
F['Xp'] = (A ^ B) ^ (C ^ D)
'''
F['NAs'] = not(A & (not(B & (not(C & D)))))
F['NAp'] = not(not(A & B) & (not(C & D)))
F['NOs'] = not(A | (not(B | (not(C | D)))))
F['NOp'] = not(not(A | B) | (not(C | D)))
'''

