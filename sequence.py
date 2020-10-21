
from qm import *

# ttStr = "0, 1, 3..7, 11.."

ttStr = "15, 14, 12, 13, 9, 8, 10, 11, 3, 2, 0, 1, 5, 4, 6, 7"

ttLst = impStr2impList(ttStr, 0)
ttLst.append(ttLst[0])
# print(ttLst)
bitLen = max(ttLst).bit_length()
ttBin = [bin(t)[2:].zfill(bitLen) for t in ttLst]
# print(ttBin)
jIn = ['0', '1', 'X', 'X']
kIn = ['X', 'X', '1', '0']

# print("\n\n")

# for s in range(len(ttLst)-1):
#     print(s, "\tttBin: ", jIn[int(ttBin[s][3] + ttBin[s+1][3],2)])

# print("\n\nttLen: ", len(ttLst))

# print("\n\n")

jTT = [[jIn[int(ttBin[n][m] + ttBin[n+1][m],2)] for m in range(bitLen)] for n in  range(len(ttLst)-1)]
kTT = [[kIn[int(ttBin[n][m] + ttBin[n+1][m],2)] for m in range(bitLen)] for n in  range(len(ttLst)-1)]

# dc = [n if n not in ttLst for n in range(2 ** bitLen)]
# print("\n\n Dont Cares: ", dc)

dc = []
for n in range(2**bitLen):
    if n not in ttLst:
        dc.append(n)
'''
print("\nDon't Cares: ", dc)

for b in range(bitLen):
    print('\n', b)
    for n in range(len(jTT)):
        print("jTT[n][b] ", jTT[n][b])

print("\n\n")

for i,jk in enumerate(zip(jTT, kTT)):
    print(str(ttLst[i]).ljust(4), end = " ")
    for j, k in zip(jk[:][0], jk[:][1]):
        print(j, k, end='  |  ')
    print('\n')

print("jtt:\n", jTT)
print("\n")
print("ktt:\n", kTT)
print("\n")
'''

# [[row[i] for row in l1] for i in range(len(l1[0]))]

# Transpose 2D Array
trX = lambda L: [[row[i] for row in L] for i in range(len(L[0]))]

print("ttLst:\n", ttLst)
print("\n")

JtrX = trX(jTT)
print("Transposed jTT:\n", JtrX)
print("\n")

KtrX = trX(kTT)
print("Transposed kTT:\n", KtrX)
print("\n")

# print([ttLst[i] for i in range(len(JtrX[1])) if JtrX[1][i] == '1'])

Jimps = [[ttLst[i] for i in range(len(JtrX[q])) if JtrX[q][i] == '1'] for q in range(len(JtrX))]
print("Jimps:\n", Jimps)
print("\n")

Jdc = [[ttLst[i] for i in range(len(JtrX[q])) if JtrX[q][i] == 'X'] for q in range(len(JtrX))]
print("Jdc:\n", Jdc)
print("\n")

Kimps = [[ttLst[i] for i in range(len(KtrX[q])) if KtrX[q][i] == '1'] for q in range(len(KtrX))]
print("Kimps:\n", Kimps)
print("\n")

Kdc = [[ttLst[i] for i in range(len(KtrX[q])) if KtrX[q][i] == 'X'] for q in range(len(KtrX))]
print("Kdc:\n", Kdc)
print("\n")

Jsop = []
for JI, JD in zip(Jimps, Jdc):
    sop = tt2ssop(JI, JD)
    for n, o in zip(["A", "B", "C", "D"], ["Q1 ", "Q2 ", "Q3 ", "Q4 "]):
        sop = sop.replace(n, o)
        sop = sop.replace("  ", " ")
    Jsop.append(sop)
#     print("\nsop: ", sop)

Ksop = []
for KI, KD in zip(Kimps, Kdc):
    sop = tt2ssop(KI, KD)
    for n, o in zip(["A", "B", "C", "D"], ["Q1 ", "Q2 ", "Q3 ", "Q4 "]):
        sop = sop.replace(n, o)
        sop = sop.replace("  ", " ")
    Ksop.append(sop)
#     print("\nsop: ", sop)

for i, (JI, KI) in enumerate(zip(Jsop, Ksop)):
    print("J" + str(i+1) + " = ", JI, "\nK" + str(i+1) + " = ", KI, "\n\n")

print("\n")

