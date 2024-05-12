# Demonstrate 16 bit Twos Compliment subtraction.
# Enter 16 bit minuend
# Enter signed 16 bit subtrahend.  -32768 .. 32768
# Result is signed 16 bit number

import numpy as np

minuend = 64206 
subtrahend = 2752

if(0):
    minuend = int(input("Enter Minuend: "))
    subtrahend = int(input("Enter Subtrahend: "))

binw = lambda N: np.array([int(b) for b in bin(N)[2:].zfill(16)])
binc = lambda N: np.array([b for b in bin(N)[2:].zfill(16)])
binHL = lambda B: np.array([B[:8], B[8:]])
onesComp = lambda B: np.array([-n+1 for n in B])
sersum = lambda B: sum([b * 2**(len(B)-1-n) for n, b in enumerate(B)])
twosCompN = lambda B: binw(2**16 - B)
bin2HexWord =  lambda B: "0x" + F"{hex(sersum(B))[2:]:0>4}"

mb = binw(minuend)
sb = binw(subtrahend)
ocb = onesComp(binw(subtrahend))
tcb = twosCompN(subtrahend)
sumb = binw(minuend + sersum(tcb))[-16:]

print(F"\nminuend   \t {mb}\t{bin2HexWord(mb)}  {eval(bin2HexWord(mb))}\n")
print(F"subtrahend\t {sb}\t{bin2HexWord(sb)}  {eval(bin2HexWord(sb))}")
print(F"ones Comp\t {ocb}\t{bin2HexWord(ocb)}  {eval(bin2HexWord(ocb))}")
print(F"twos Comp\t {tcb}\t{bin2HexWord(tcb)}  {eval(bin2HexWord(tcb))}")
print('')
print(F"minuend   \t {mb}\t{bin2HexWord(mb)}  {eval(bin2HexWord(mb))}")
print(F"twos Comp\t+{tcb}\t{bin2HexWord(tcb)}  {eval(bin2HexWord(tcb))}")
print(F"      Sum\t {sumb}\t{bin2HexWord(sumb)}  {eval(bin2HexWord(sumb))}")

print(F"\n{minuend} - {subtrahend} = {sersum(sumb)}\n")

'''
-------------------------------------------------------------------------------
Example minuend = 64206  subtrahend = 2752
Output:
minuend   	 [1 1 1 1 1 0 1 0 1 1 0 0 1 1 1 0]	0xface  64206

subtrahend	 [0 0 0 0 1 0 1 0 1 1 0 0 0 0 0 0]	0x0ac0  2752
ones Comp	   [1 1 1 1 0 1 0 1 0 0 1 1 1 1 1 1]	0xf53f  62783
twos Comp	   [1 1 1 1 0 1 0 1 0 1 0 0 0 0 0 0]	0xf540  62784

minuend   	 [1 1 1 1 1 0 1 0 1 1 0 0 1 1 1 0]	0xface  64206
twos Comp	  +[1 1 1 1 0 1 0 1 0 1 0 0 0 0 0 0]	0xf540  62784
      Sum	   [1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 0]	0xf00e  61454

64206 - 2752 = 61454
'''
