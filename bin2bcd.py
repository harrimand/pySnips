#!/usr/bin/env python3.8

from os import sys

def getInput():
    N = -1
    while((N < 0) | ( N > 255)):
        binIn = input("\nEnter Binary Number <= 255: ")
        if (binIn.count('0') + binIn.count('1') == len(binIn)):
            N = int(binIn, 2)
            print("\n\tYou entered: ", binIn)
            print("\n\t", binIn , "binary = ", N, " decimal")
    return N


if(len(sys.argv) > 1):
    binIn = sys.argv[1]
    if (binIn.count('0') + binIn.count('1') == len(binIn)):
        if(int(binIn, 2) < 256):
            N = int(binIn, 2)
        else:
            N = getInput()
    else:
        N = getInput()
else:
    N = getInput()

print("\n\n\tDouble Dabble Algorithm:")
print("\t\tShift left.  if (BCD digit > 4): add 3 to BCD digit")

N = N << 3
print("\n\n\tShifting left 3 times before BCD Ones digit could be > 4")
print("\n\t Huns   Tens   Ones   Input", end="")

Nb = bin(N)[2:].zfill(20)
print("\n\t", Nb[-20:-16], ' ', Nb[-16:-12], ' ', Nb[-12:-8], ' ', bin(N)[-8:])

for _ in range(5):
    H = (N & (15 * 2**16)) >> 16
    if (H > 4):
        N = N + (3<<16)
        print("\tHundreds ", H , ' + 3 = ', H + 3)
    else:
        print("\tHundreds = ", H)

    T = (N & (15 * 2**12)) >> 12
    if (T > 4):
        N = N + (3<<12)
        print("\t    Tens ", T , ' + 3 = ', T + 3)
    else:
        print("\t    Tens = ", T)

    O = (N & (15 * 2**8)) >> 8
    if(O > 4):
        N = N + (3<< 8)
        print("\t    Ones ", O , ' + 3 = ', O + 3)
    else:
        print("\t    Ones = ", O)

    Nb = bin(N)[2:].zfill(20)
    print("\t", Nb[-20:-16], ' ', Nb[-16:-12], ' ', Nb[-12:-8], ' ', bin(N)[-8:])
    N = N << 1
    print('\n\t<< 1\n')
    Nb = bin(N)[2:].zfill(20)
    print("\t", Nb[-20:-16], ' ', Nb[-16:-12], ' ', Nb[-12:-8], ' ', bin(N)[-8:])


H = (N & (15 * 2**16)) >> 16
T = (N & (15 * 2**12)) >> 12
O = (N & (15 * 2**8)) >> 8

print("\tHundreds = ", H)
print("\t    Tens = ", T)
print("\t    Ones = ", O)
print("\n\n")


