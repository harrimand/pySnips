import numpy as np
from os import system
cls = lambda: system("clear") # Replace "clear" with "cls" for windows.

''' 16 bit values to bitwise XOR to toggle LEDs diagonal
    to selected button position in 4x4 matrix'''
act = {
    0: 0x8421, 1: 0x4A10, 2: 0x2850, 3: 0x1248,
    4: 0x4842, 5: 0xA4A1, 6: 0x5258, 7: 0x2124,
    8: 0x2484, 9: 0x1A4A, 10: 0x8525, 11: 0x4212,
    12: 0x1248, 13: 0x01A4, 14: 0X0852, 15: 0x8421}

# X not used in this program but may be copied to Arduino progmem 
X = [
    0x8421, 0x4A10, 0x2850, 0x1248,
    0x4842, 0xA4A1, 0x5258, 0x2124,
    0x2484, 0x1A4A, 0x8525, 0x4212,
    0x1248, 0x01A4, 0X0852, 0x8421]

def grid(M):
    ''' Display 4x4 matrix of 1s/0s in 16 bit binary (M)'''
    print('\n')
    bM = bin(M)[2:].zfill(16)
    R = [bM[n*4: n*4+4] for n in range(4)]
    for r in R:
        print('\t', end='')
        for b in r:
            print(b, end='  ')
        print('\n')

def B(m, n, verb):
    ''' Bitwise XOR n with m and return result.
    If verb = true display matrix using grid()'''
    m = m^act[n]
    if(verb):
        grid(m)
    return m

def Bseq(m, seq, verb=True):
    ''' Sequentially XOR each item in seq with m
    Update m with each XOR operation.  pass
    verb (verbose) to B() to display each matrix or not'''
    for s in seq:
        m = B(m, s, verb)
    return m

def countBits(M, bits):
    ''' Count number of bits set in binary(M) matching
    bit postions in list(bits)'''
#    bM = bin(M)[2:].zfill(16)
    n = 0
    for b in bits:
        n = n+1 if M & 2**(15-b) else n
    return n

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
#    print('\n')
    return buttonSeq

def solve(M, verb=True):
    ''' Get solution key sequence and apply XOR with value for
    each key in sequence.  if verb == True display matrix
    after each XOR operation. Return result after all operations'''
    K = keyChk(M, verb)
    if(verb):
        print('\t',K)
        grid(M)
    M = Bseq(M, K, verb)
    return M

def solvable():
    ''' Return list of all completely solvable starting values.
    Solved condition is met when All LEDs are on'''
    ev = [n for n in range(65536) if bin(n)[2:].count('1')%2 == 0]
    ssL = []
    for e in ev:
        ss = solve(e, False)
        if(ss == 65535):
            ssL.append(e)
    return ssL

def DiagZeros():
    ''' Return list of all starting values that result in matrix
    where positions [3, 6, 9, 12] are 0.  Button 3 or 12 B(m, 3) or
    B(m, 12) will complete the solution'''
    ev = [n for n in range(65536) if bin(n)[2:].count('1')%2 == 0]
    diaR = []
    for e in ev:
        ss = solve(e, False)
        if(ss == 60855):
            diaR.append(e)
    return diaR

# Dictionary containing {Matrix_Value: [Solution key sequence]}
#    for all Matrix_values in M
keySeqs = lambda M: {s:keyChk(s, False) for s in M}

# Dictionary of {Matrix_Values: [Solution key sequence]}
#    for all solvable Matrix Values.
Sdict = {k:dz for k, dz in keySeqs(solvable()).items()}

# Dictionary of {Matrix_Values: [Solution key sequence]}
#    for all Matrix Values resulting in diagonal zeros when solved.
DZdict = {k:dz + [3] for k, dz in keySeqs(DiagZeros()).items()}


# deprecated.  Use keyChk() instead.
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


# M = int("1010"*4, 2)
M = 0x7EDB


