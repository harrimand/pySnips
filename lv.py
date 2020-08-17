

from qm import *
import numpy as np
from logic.logic import *
import matplotlib.pyplot as plt

class lv():
    def __init__(self, numBits):
        self.nb = numBits
        self.tt = ttIn(numBits)
        self.Labels = []

    def ttIn(self, nb):
        self.tt = [[int(b) for b in np.array(list(bin(n)[2:].zfill(self.nb)))] for n in np.arange(2 ** self.nb)]
    
    def cols(self):
        return list(map(list, zip(*self.tt)))

    def newCol(self, newCols):
        self.tt = np.hstack((self.tt, list(map(list, zip(*newCols)))))

    def plotLabels(self, labels):
        lblList = []
        for h, L in enumerate(labels):
            lblList.append(plt.text(-.5, h*2+1.25, L, fontsize=20, fontweight="bold"))
        self.Labels = lblList

    def logicPlot(self, Labels=[]):
        bitSize = len(Q[0])
        Q = np.transpose(self.tt)
        bSx = []
        bSy = []
        for S in Q:
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

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        fig.set_size_inches(18, 6, forward=True)

        sY = [[B + N * 2 for B in bSy[N]] for N in range(bitSize)]
    #     print(sY)

        # Data Plots
        for n in range(bitSize):
            ax.plot(bSx[n], sY[n], linewidth=3)

        # Stem Plot Markers
        for n in range(2**numBits):
            plt.plot([n+.5, n+.5], [0, 2**(bitSize-1)], ':r')

        ax.set_title("Logic Plot", fontsize=20, fontweight="bold")
        # ax.set_ylabel("<--Msb---Lsb-->", fontsize=16)
        ax.xaxis.grid(False)
        ax.yaxis.grid(True)
        ax.set_yticklabels([])
        ax.set_xticks([n for n in range(2**numBits + 1)])
        ax.set_ylim(0, bitSize * 2)

    #     Labels = ["A", "B", "C", "D", "A$\oplus$C", "B$\oplus$D", "(A$\oplus$C) & (B$\oplus$D)"]
        plotLabels(Labels)

        plt.text(1, -.75, "Plotted using Python and Matplotlib by Darrell Harriman", fontweight="bold")

        plt.ion()

        plt.show()


T = lv(4)
print(T.tt)
A, B, C, D = T.cols()
print("\n", A)
print("\n", B)
print("\n", C)
print("\n", D)

x1 = XOR(A, C)
x2 = XOR(B, D)
x3 = AND(x1, x2)

T.newCol([x1, x2, x3])

print("\t\t")
for t in T.tt:
    print(t)

T.logicPlot()


