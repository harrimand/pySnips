

import numpy as np
from os import system
from itertools import combinations

cls = lambda: system("clear") # Replace "clear" with "cls" for windows.

''' 16 bit values to bitwise XOR to toggle LEDs diagonal
    to selected button position in 4x4 matrix'''
act = {
    0: 0x8421, 1: 0x4A10, 2: 0x2850, 3: 0x1248,
    4: 0x4842, 5: 0xA4A1, 6: 0x5258, 7: 0x2124,
    8: 0x2484, 9: 0x1A4A, 10: 0x8525, 11: 0x4212,
    12: 0x1248, 13: 0x01A4, 14: 0X0852, 15: 0x8421}

# Dictionary of keys: [[Count String], [LED positions],[Number of LEDs]]
nt = ["None or two of ", "One of "]
sqChk = {
        0:[[nt[0]],[0, 8, 13],[0, 2]],
        1:[[nt[1]],[3, 6],[1]],
        3:[[nt[0]],[0, 6, 9],[0, 2]],
        4:[[nt[1]],[3, 9],[1]],
        5:[[nt[0]],[5, 8, 10],[0, 2]],
        6:[[nt[0]],[1, 6, 9],[0, 2]],
        8:[[nt[1]],[0, 5],[1]],
        9:[[nt[0]],[4, 6, 9],[0, 2]],
        10:[[nt[0]],[5, 10, 13],[0, 2]],
        13:[[nt[1]],[0, 10],[1]]}

def countBits(M, bits):
    ''' Count number of bits set in binary(M) matching
    bit postions in list(bits)'''
#    bM = bin(M)[2:].zfill(16)
    n = 0
    for b in bits:
        n = n+1 if M & 2**(15-b) else n
    return n

def grid(M):
    ''' Display 4x4 matrix of 1s/0s in 16 bit binary (M)'''
    print(M, "  " + hex(M))
    bM = bin(M)[2:].zfill(16)
    R = [bM[n*4: n*4+4] for n in range(4)]
    for r in R:
        gridRow = '\t'+' '.join([ch for ch in r])
        print(gridRow)
#    print('\n')

def B(M, seq, verb=True):
    ''' Bitwise XOR n with m and return result.
    If verb = true display matrix using grid()'''
    seq = seq if isinstance(seq, list) else [seq]
    for s in seq:
        M = M^act[s]
        if(verb):
            print(s, end=' ')
            grid(M)
    return M

def keyChk(M, verb=True):
    ''' if verb == True: display list of button positions to press
    if required number of leds are set from list of LED positions.
    Return sequence of keys to solve puzzle'''
    if(verb):
        print("\tSolving:")
    buttonSeq = []
    for key, LED in sqChk.items():
        LEDmatch = countBits(M, LED[1]) in LED[2]
        leds = ' '.join([str(l) for l in LED[1]])
        if(verb):
            print("\t", key, "\t", (LED[0][0]+leds).ljust(26), end='')
            print("Y" if LEDmatch else "-")
        if LEDmatch:
            buttonSeq.append(key)
    return buttonSeq

bcomb = [list(combinations(list(range(16)), n)) for n in range(1,10)]
# bcombL = [[list(t) for t in tlist] for tlist in bcomb]
bcombL = [[list(t) for t in tL] for tL in bcomb]

for i, m in enumerate(bcombL):
    for j, n in enumerate(m):
        if(3 in n and 12 in n):
            # print(n)
            bcombL[i].remove(bcombL[i][j])
        if(0 in n and 15 in n):
            # print(n)
            bcombL[i].remove(bcombL[i][j])
            # bcombL[i].remove(n)

Bst = []
for BC in bcombL:
    bn = []
    for bc in BC:
        bn.append(B(0xFFFF, bc, False))
    Bst.append(bn)

'''
for n in range(9):
    for m in Bst[n]:
        while(Bst[n].count(m) > 1):
            Bst[n].remove(m)
'''
solLen = [len(b) for b in Bst]

BLlens = [len(b) for b in bcombL]
bcLens = [16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440]




