#!/usr/bin/env python3.8

import numpy as np
import matplotlib.pyplot as plt

# Data = [3, 5, 17, 29, 63, 165, 90, 8]
# Data = [83, 116, 101, 118, 101, 32, 75, 117, 114, 116, 105]
# Data = [68, 97, 114, 114, 101, 108, 108, 32, 72, 97, 114, 114, 105, 109, 97, 110]
# Data =[11, 10, 11, 15, 11,  5,  7,  4,  1,  7, 11,  9, 13, 15,  8,  5,  7,  3,  2,
#  9, 11, 9, 14, 13, 6, 6, 6, 1, 4, 11]

# Data = [1, 0, 1, 0, 1, 1, 1, 0]

NandData = [1, 3, 1, 3, 6, 7, 6, 7, 1, 3, 1, 3, 6, 7, 6, 7]
# Data = [0, 6, 4, 6, 4, 1, 0, 1, 1, 0, 0, 6, 6, 4, 4, 6, 4, 1, 0, 1, 0]
Data = [0, 4, 0, 4, 0, 2, 2, 14, 10, 14, 10, 8, 9, 5, 1, 5, 1, 0]

dataStr = "Darrell Harriman"
# dataStr = "Nelian Harriman"
# dataStr = "Roy Estabrook"
# dataStr = "Steve Kurti"
# dataStr = "Paul Tonning"
# dataStr = "Khalid Rubayi"

bitSize = max(Data).bit_length()
parallel = False

text2data = lambda txt: [ord(c) for c in txt]

try:
	Data
except NameError:
	Data = text2data(dataStr)

serStreamS = np.array([[int(b) for b in bin(N)[2:].zfill(bitSize)] for N in Data])

if(not(parallel)):
    serStream = np.transpose(serStreamS)

print('\n\n')
nl = 0
for S, B in zip(Data, serStreamS):
    print('\t', str(S).rjust(5), B, end=' ')
    nl += 1
    if ((nl % 3) == 0):
        print('\n')

print('\n\n')

bSx = []
bSy = []
for S in serStream:
    bTemp = []
    t = 0
    bSt = []
    for b, b2 in zip(S[:-1], S[1:]):
        bTemp.append(b)
        bSt.append(t)
        t = t + 1
        if [b, b2] == [1, 0]:
            bTemp.append(1)
            bSt.append(t)
        elif [b, b2] == [0, 1]:
            bTemp.append(0)
            bSt.append(t)
#        print(b, b2, end='  ')
    bTemp.append(S[-1])
    bTemp.append(S[-1])
    bSt.append(t)
    bSt.append(t+1)
    bSy.append(bTemp)
    bSx.append(bSt)
#    print(bTemp, end=' ')
#    print(" bSt: ", bSt, end=' ')
#    print(f" ({len(bTemp)}, {len(bSt)})")
#    print('\n')

# print('\n\n')
if(0):
    for S, x, y in zip(serStream, bSx, bSy):
        print(S)
        print(y)
        print(x)
        print('\n')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fig.set_size_inches(18, 6, forward=True)

sY = [[B + N * 2 for B in bSy[N]] for N in range(bitSize)]
print(sY)

for n in range(bitSize):
#    sY = [bSy[N] + N * 2 for N in bSy[n]]
    ax.plot(bSx[n], sY[n], linewidth=3)

for n in range(len(Data)):
#    plt.text(n+.5, 2 * bitSize, str(Data[n]), fontsize=16)
    plt.plot([n+.5, n+.5], [0, 2**(bitSize-1)], ':r')

ax.set_title("S-R Latch Inputs/Output", fontsize=16)
# ax.set_ylabel("<--Msb---Lsb-->", fontsize=16)
ax.xaxis.grid(False)
ax.yaxis.grid(True)
ax.set_yticklabels([])
ax.set_xticks([n for n in range(len(Data)+1)])
ax.set_ylim(0, bitSize * 2)
plt.text(-.5, 6.5, "R", fontsize=20, fontweight="bold")
plt.text(-.5, 4.5, "S", fontsize=20, fontweight="bold")
plt.text(-.5, 2.5, "E", fontsize=20, fontweight="bold")
plt.text(-.5, .5, "Q", fontsize=20, fontweight="bold")

plt.text(1, -.5, "Plotted using Python and Matplotlib by Darrell Harriman", fontweight="bold")

plt.show()


