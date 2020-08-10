
import numpy as np
from qm import *

# input = np.array([list(bin(n)[2:].zfill(7)) for n in range(100)], dtype='int')

nb1 = np.array([list(bin(n%10)[2:].zfill(4)) for n in range(100)], dtype='int')
nb10 = np.array([list(bin(n//10)[2:].zfill(4)) for n in range(100)], dtype='int')

nb = np.array([[m, n] for m, n in zip(nb10, nb1)])

nbtt10 = [list(np.where(nb[:,0,b]==1)[0]) for b in range(4)]
nbtt1 = [list(np.where(nb[:,1,b]==1)[0]) for b in range(4)]

Vars = [chr(c) for c in range(65, 72)]

dcStr = "100.."
dc = impStr2impList(dcStr)

ssopt = [tt2ssop(nbtt10[n], dc) for n in range(4)]

ssopo = [tt2ssop(nbtt1[n], dc) for n in range(4)]

print("\n\nTens:")

for b, t in enumerate(ssopt):
    print("\nbit ", 3-b)
    print(t)

print("\n\nOnes:")

for b, t in enumerate(ssopo):
    print("\nbit ", 3-b)
    print(t)

print("\n\nTens:\n")

for n in range(4):
    print("bit ", 3-n, ssopt[n])
    print(sop2imps(ssopt[n],Vars))
    print("\n\n")


print("\n\nOnes:\n")

for n in range(4):
    print("bit ", 3-n, ssopo[n])
    print(sop2imps(ssopo[n],Vars))
    print("\n\n")

print("\n\n")

