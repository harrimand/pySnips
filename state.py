
from qm import *

ttStr = "0, 1, 3..7, 11.."
ttLst = impStr2impList(ttStr)

ttLst.append(ttLst[0])
print(ttLst)
bitLen = max(ttLst).bit_length()
ttBin = [bin(t)[2:].zfill(bitLen) for t in ttLst]
print(ttBin)

jIn = ['0', '1', 'X', 'X']
kIn = ['X', 'X', '1', '0']

print("\n\n")

for s in range(len(ttLst)-1):
    print(s, "\tttBin: ", jIn[int(ttBin[s][3] + ttBin[s+1][3],2)])


print("\n\nttLen: ", len(ttLst))

print("\n\n")

jTT = [[jIn[int(ttBin[n][m] + ttBin[n+1][m],2)] for m in range(bitLen)] for n in  range(len(ttLst)-1)]
kTT = [[kIn[int(ttBin[n][m] + ttBin[n+1][m],2)] for m in range(bitLen)] for n in  range(len(ttLst)-1)]

'''
for i,j in enumerate(jTT):
    print(i, j)

print("\n\n")

for i,k in enumerate(kTT):
    print(i, k)

print("\n\n")
'''
# for i, n in enumerate(zip(range(1,11), range(2,12))):
#     print(i, n[0], n[1])

print("\n\n")

for i,jk in enumerate(zip(jTT, kTT)):
    print(str(ttLst[i]).ljust(4), end=' ')
    for j, k in zip(jk[:][0], jk[:][1]):
        print(j, k, end='  |  ')
    print('\n')

