
from cistercian import *

PiStr = '3.141592653589793238462643383279502884197169399375105820974944592307816406286'

Pi75 = PiStr[2:]
ch = []
n = 0
while(n < (len(Pi75) - 3)):
    ch.append(Pi75[n:n+4])
    n = n + 4

PiCh1 = cistChars([3] + ch[:5])
PiCh2 = cistChars(ch[5:11])
PiCh3 = cistChars(ch[11:17])

ch06 = ['3'] + ch[:5]
print('\t ', end='')
for c in ch06:
    print(c.ljust(14), end='')
printMat(PiCh1)

print('\t ', end='')
for c in ch[5:11]:
    print(c.ljust(14), end='')
printMat(PiCh2)

print('\t ', end='')
for c in ch[11:17]:
    print(c.ljust(14), end='')
printMat(PiCh3)


