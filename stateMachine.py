
from qm_ import *
import numpy as np
import pandas as pd
from os import system
cls = lambda: system("clear")

jj = ["0", "1", "X", "X"]
kk = ["X", "X", "1", "0"]

seqLen = 12
# seq = np.array(np.random.permutation(seqLen), dtype=int)
# seq = np.array([4,7,5,6,0,2,1,3], dtype=int)

# seqS = "..3 5 6 8..11 13 15"
seqS = "8 12 14 15 11 9 4 6 7 3 1 0 2 10 13 5"

seq = impStr2impList(seqS)

seq1 = np.roll(seq, -1)

steps = np.array([[m, n] for m, n in zip(seq, seq1)])

ml = max(seq)
bitlen = int(ml).bit_length()

stepsBin = np.array([[list(bin(m)[2:].zfill(bitlen)),list(bin(n)[2:].zfill(bitlen))] for m, n in zip(seq,seq1)])

jkIn = [jk.transpose() for jk in stepsBin]
jkInD = [[int(b[0]+b[1],2) for b in step] for step in jkIn]

J = {s: [jj[d] for d in step] for s, step in zip(seq, jkInD)}
K = {s: [kk[d] for d in step] for s, step in zip(seq, jkInD)}

seqSorted = sorted(seq)
Jsorted = {s: J[s] for s in sorted(J.keys())}
Ksorted = {s: K[s] for s in sorted(K.keys())}

Q = ["Q" + str(n) for n in range(bitlen-1,-1,-1)]

Jhead = ["J" + str(n) for n in range(int(ml).bit_length()-1,-1,-1)]
Khead = ["K" + str(n) for n in range(int(ml).bit_length()-1,-1,-1)]

jn = np.array(list(Jsorted.values())).transpose()
kn = np.array(list(Ksorted.values())).transpose()

Jdf = pd.DataFrame(jn.transpose(), index=Jsorted.keys(), columns=Jhead)
Kdf = pd.DataFrame(kn.transpose(), index=Ksorted.keys(), columns=Khead)

cols = [int(n/2) + n%2 * bitlen for n in range(2*bitlen)]
JKcat = pd.concat([Jdf, Kdf], axis=1)

JKtable = JKcat.iloc[:, cols]

JKimps=lambda C: [int(n) for n, i in zip(Jsorted,JKtable[C]) if i=='1']
JKdc=lambda C: [int(n) for n, i in zip(Jsorted,JKtable[C]) if i=='X']

J3sops = {Jh: qmSimp(JKimps(Jh), JKdc(Jh)) for Jh in Jhead}
K3sops = {Kh: qmSimp(JKimps(Kh), JKdc(Kh)) for Kh in Khead}

def Qspc(sop):
    sop = sop.replace("!", " !")
    sop = sop.replace("Q", " Q")
    sop = sop.replace("  Q", " Q")
    sop = sop.replace("! Q", "!Q")
    return sop

def subQ(sop):
    for n, qn in enumerate(Q):
        sop = sop.replace(chr(n+65), qn)
    sop = "0" if len(sop) == 0 else sop
    sop = Qspc(sop)
    return sop

def shSOPs():
    print(F"\n\tSequence: {seqS}\n")
    for j, k in zip(list(J3sops.keys()), list(K3sops.keys())):
        print(F"\t{j} = {subQ(J3sops[j])}")
        print(F"\t{k} = {subQ(K3sops[k])}")



shSOPs()



