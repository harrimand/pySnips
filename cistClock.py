
import matplotlib.pyplot as plt
import numpy as np
import time

# plt.ion()

fig = plt.figure(figsize=(6, 3), facecolor='k')
ax = plt.axes()
ax.set_facecolor('b')

lw = 4 # linewidth

plt.axis('off')

bx = [.5, 10.5, 10.5, .5, .5]
by = [.5, .5, 8.5, 8.5, .5]
pb = plt.plot(bx, by, c='g')

pc1 = plt.plot([3, 3], [1, 8], c='m', linewidth=lw)
pc2 = plt.plot([8, 8], [1, 8], c='m', linewidth=lw)

sR1= [[[],[]],[[8,10],[8, 8]], [[8, 10], [5, 5]], [[8, 10], [8, 5]],
     [[8, 10], [5, 8]], [[8, 10, 8], [5, 8, 8]], [[10, 10], [8, 5]],
     [[8, 10, 10], [8, 8, 5]], [[8, 10, 10], [5, 5, 8]],
     [[8, 10, 10, 8],[8, 8, 5, 5]]]

sR1xm5 = [[]] + [[n-5 for n in m] for m in [s[0] for s in sR1[1:]]]
sR1y = [[]] + [[n for n in m] for m in [s[1] for s in sR1[1:]]]
sL1 = [m for m in zip(sR1xm5, sR1y)]

sR10x = [[]] + [[16 - n for n in m] for m in [s[0] for s in sR1[1:]]]
sR1y = [[]] + [[n for n in m] for m in [s[1] for s in sR1[1:]]]
sR10 = [m for m in zip(sR10x, sR1y)]

sR10xm5 = [[]] + [[n-5 for n in m] for m in [s[0] for s in sR10[1:]]]
sR10y = [[]] + [[n for n in m] for m in [s[1] for s in sR1[1:]]]
sL10 = [m for m in zip(sR10xm5, sR10y)]

sR100x = [[]] + [[n for n in m] for m in [s[0] for s in sR1[1:]]]
sR100y = [[]] + [[9 - n for n in m] for m in [s[1] for s in sR1[1:]]]
sR100 = [m for m in zip(sR100x, sR100y)]

sL100xm5 = [[]] + [[n-5 for n in m] for m in [s[0] for s in sR100[1:]]]
sL100y = [[]] + [[n for n in m] for m in [s[1] for s in sR100[1:]]]
sL100 = [m for m in zip(sL100xm5, sL100y)]

sR1000x = [[]] + [[n for n in m] for m in [s[0] for s in sR10[1:]]]
sR1000y = [[]] + [[9 - n for n in m] for m in [s[1] for s in sR10[1:]]]
sR1000 = [m for m in zip(sR1000x, sR1000y)]

sL1000x = [[]] + [[n for n in m] for m in [s[0] for s in sL10[1:]]]
sL1000y = [[]] + [[9 - n for n in m] for m in [s[1] for s in sL10[1:]]]
sL1000 = [m for m in zip(sL1000x, sL1000y)]

sR = [sR1000, sR100, sR10, sR1]
sL = [sL1000, sL100, sL10, sL1]


pR1 = lambda n: plt.plot(sR1[n][0], sR1[n][1], c='y', linewidth=lw)
pR10= lambda n: plt.plot(sR10[n][0], sR10[n][1], c='y', linewidth=lw)
pL1 = lambda n: plt.plot(sL1[n][0], sL1[n][1], c='y', linewidth=lw)
pL10 = lambda n: plt.plot(sL10[n][0], sL10[n][1], c='y', linewidth=lw)
pR100 = lambda n: plt.plot(sR100[n][0], sR100[n][1], c='y', linewidth=lw)
pL100 = lambda n: plt.plot(sL100[n][0], sL100[n][1], c='y', linewidth=lw)
pR1000 = lambda n: plt.plot(sR1000[n][0], sR1000[n][1], c='y', linewidth=lw)
pL1000 = lambda n: plt.plot(sL1000[n][0], sL1000[n][1], c='y', linewidth=lw)

pR = [pR1000, pR100, pR10, pR1]
pL = [pL1000, pL100, pL10, pL1]

def cistDisp(tL, tR):
    P = [0 for n in range(8)]
    for i, d in enumerate(str(tL).zfill(4)):
        P[i] = pL[i](int(d))
    for i, d in enumerate(str(tR).zfill(4)):
        P[i+4] = pR[i](int(d))
    return P

PLR = cistDisp(706, 659)

plt.show()

'''
for n in range(10):
    PLR[7][0].set_data(sR1[n][0], sR1[n][1])
    time.sleep(1)
    plt.show(block=False)
'''

for xy in PLR:
    print(plt.get(xy[0], 'xdata'), plt.get(xy[0], 'ydata'))











