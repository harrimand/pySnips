
from os import system
cls = lambda: system("clear")

act = {
    0: 0x8421, 1: 0x4A10, 2: 0x2850, 3: 0x1248,
    4: 0x4842, 5: 0xA4A1, 6: 0x5258, 7: 0x2124,
    8: 0x2484, 9: 0x1A4A, 10: 0x8525, 11: 0x4212,
    12: 0x1248, 13: 0x01A4, 14: 0X0852, 15: 0x8421}

X = [
    0x8421, 0x4A10, 0x2850, 0x1248,
    0x4842, 0xA4A1, 0x5258, 0x2124,
    0x2484, 0x1A4A, 0x8525, 0x4212,
    0x1248, 0x01A4, 0X0852, 0x8421]

def grid(M):
    print('\n')
    bM = bin(M)[2:].zfill(16)
    R = [bM[n*4: n*4+4] for n in range(4)]
    for r in R:
        print('\t', end='')
        for b in r:
            print(b, end='  ')
        print('\n')

def B(m, n):
    m = m^act[n]
    grid(m)
    return m

def Bseq(m, seq):
    for s in seq:
        m = B(m, s)
    return m

def countBits(M, bits):
#    bM = bin(M)[2:].zfill(16)
    n = 0
    for b in bits:
        n = n+1 if M & 2**(15-b) else n
    return n

# M = int("1010"*4, 2)
M = 0x7EDB

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

def keyChk(M):
    print("\tSolving:")
    buttonSeq = []
    for key, LED in sqChk.items():
        LEDmatch = countBits(M, LED[1]) in LED[2]
        leds = ' '.join([str(l) for l in LED[1]])
        print("\t", key, "\t", (LED[0][0]+leds).ljust(26), end='')
        print("Y" if LEDmatch else "-")
        if LEDmatch:
            buttonSeq.append(key)
    print('\n')
    return buttonSeq


def hlp(M):
    print("\tSolving:")
    print("\t0   None or two of 0, 8, 13".ljust(30), end=' ')
    print(" Y" if(countBits(M,[0,8,13]) in [0,2]) else " n")
    print("\t1   One of 3, 6".ljust(30), end=' ')
    print(" Y" if(countBits(M,[3,6]) in [1]) else " n")
    print("\t3   None or two of 3, 6, 9".ljust(30), end=' ')
    print(" Y" if(countBits(M,[3,6,9]) in [0,2]) else " n")
    print("\t4   One of 3, 9".ljust(30), end=' ')
    print(" Y" if(countBits(M,[3,9]) in [1]) else " n")
    print("\t5   None or two of 5, 8, 10".ljust(30), end=' ')
    print(" Y" if(countBits(M,[5,8,10]) in [0,2]) else " n")
    print("\t6   None or two of 1, 6, 9".ljust(30), end=' ')
    print(" Y" if(countBits(M,[1,6,9]) in [0,2]) else " n")
    print("\t8   One of 0, 5".ljust(30), end=' ')
    print(" Y" if(countBits(M,[0,5]) in [1]) else " n")
    print("\t9   None or two of 4, 6, 9".ljust(30), end=' ')
    print(" Y" if(countBits(M,[4,6,9]) in [0,2]) else " n")
    print("\t10  None or two of 5, 10, 13".ljust(30), end=' ')
    print(" Y" if(countBits(M,[5,10,13]) in [0,2]) else " n")
    print("\t13  One of 0, 10".ljust(30), end=' ')
    print(" Y" if(countBits(M,[0,10]) in [1]) else " n")




