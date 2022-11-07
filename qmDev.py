
from random import shuffle
import numpy as np

from os import system
cls = lambda: system("clear")

def rndBitLength(n, bl):
    if n <= 2**n:
        seq = [s for s in range(2**bl)]
        shuffle(seq)
        return seq[:n]
    return [0]

def dispDF(df):
    for d in df:
        print('\t', d, '\t', df[d])
    print('\n')

def bitmatch(sq):
    res = []
    for n in range(len(sq)-1):
        cell = []
        for d, f in zip(sq[n], sq[n+1]):
            x = d^f
            if(bin(x).count("1") == 1):
                cell.append((d, f))
        res.append(cell)
    return res


seq = lambda bl: [n for n in range(2**bl)]
#shuffle(seq)


sq4 = seq(4)
shuffle(sq4)
sq4n = np.array(sq4, dtype=int)




# blsort = {c:sq4n[[bin(n).count("1") == c for n in sq4n]] for c in range(max(seq.bit_length()))}

bitSort = lambda sq: {c:sq[[bin(n).count("1") == c for n in sq]] for c in range(int(max(sq)).bit_length()+1)}


