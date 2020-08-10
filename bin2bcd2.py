

import numpy as np
from qm import *

# input = np.array([list(bin(n)[2:].zfill(7)) for n in range(100)], dtype='int')

nb1 = np.array([list(bin(n%10)[2:].zfill(4)) for n in range(256)], dtype='int')
nb10 = np.array([list(bin((n//10)%10)[2:].zfill(4)) for n in range(256)], dtype='int')
nb100 = np.array([list(bin(n//100)[2:].zfill(4)) for n in range(256)], dtype='int')
'''
for n in nb100:
    print(n)
'''
print('\n\n')

nb = np.array([[m, n, o] for m, n, o in zip(nb100, nb10, nb1)])

nbtt100 = [list(np.where(nb[:,0,b]==1)[0]) for b in range(2, 4)]
nbtt10 = [list(np.where(nb[:,1,b]==1)[0]) for b in range(4)]
nbtt1 = [list(np.where(nb[:,2,b]==1)[0]) for b in range(4)]

Vars = [chr(c) for c in range(65, 73)]

btt100 = [[int(n) for n in m] for m in nbtt100]
btt10 = [[int(n) for n in m] for m in nbtt10]
btt1 = [[int(n) for n in m] for m in nbtt1]

'''
print(btt10)
print('\n\n')

print(nbtt10[0])
print(nbtt10[1])
print('\n\n')
print(nbtt100[0])
print(nbtt100[1])
'''

# dcStr = ""
# dc = impStr2impList(dcStr)
dc = []
ssoph = [tt2ssop(btt100[n], dc) for n in range(2)]
# print('\n\n')
# print(tt2ssop(btt10[0], dc))

ssopt = [tt2ssop(btt10[n], dc) for n in range(4)]

ssopo = [tt2ssop(btt1[n], dc) for n in range(4)]

def logisim(sop):
    """ Insert spaces between variables for Logisim compatibility"""
    return " ".join(list(sop)).replace('! ', '!').replace('  +  ', ' + ')


#------------------------------------------------------------------------------
with open("bin2bcd.txt", 'w') as bcd:
    bcd.write("\n\nHundreds:")
    print("\n\nHundreds:")

    for b, t in enumerate(ssoph):
        print("\nbit ", 1-b)
        print(logisim(t))
        bcd.write("\n\nbit " + str(1-b) + "\n")
        bcd.write(logisim(t))

    print("\n\nTens:")
    bcd.write("\n\nTens:")

    for b, t in enumerate(ssopt):
        print("\nbit ", 3-b)
        print(logisim(t))
        bcd.write("\n\nbit " + str(3-b) + "\n")
        bcd.write(logisim(t))

    print("\n\nOnes:")
    bcd.write("\n\nOnes:")

    for b, t in enumerate(ssopo):
        print("\nbit ", 3-b)
        print(logisim(t))
        bcd.write("\n\nbit " + str(3-b) + "\n")
        bcd.write(logisim(t))

#------------------------------------------------------------------------------
print("\n\nHundreds:\n")

for n in range(2):
    print("bit ", 1-n, ssoph[n])
    print(sop2imps(ssoph[n],Vars))
    print("\n\n")

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


