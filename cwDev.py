

import numpy as np
import matplotlib.pyplot as plt
from random import randint
from  matplotlib.animation import FuncAnimation

from os import system
cls = lambda: system("clear")

rndGrid = lambda r, c: np.array([[randint(0,1) for n in range(c)] for m in range(r)])

# cw = rndGrid(8, 10)

ax = [(r,c) for r in [-1, 0, 1] for c in [-1, 0, 1] if (r!=0) or (c!=0)]

cwSum = lambda cw: np.sum([np.roll(cw, a, (0, 1)) for a in ax], 0)

# np.logical_or(np.logical_and(cw == 1, cnt == 2), cnt == 3)*1

def newGen(cw):
    cnt = cwSum(cw)
    return np.logical_or(np.logical_and(cw == 1, cnt == 2), cnt == 3)*1


plot = plt.matshow(cw)

def init():
    plot.set_data(cw)
    return plot

def update(j):
    plot.set_data(cw)
    return [plot]


# anim = FuncAnimation(fig, update, init_func = init, frames=n_frames, interval = 30, blit=True)

plt.show()


def testcw(r, c=0):
    if c == 0:
        c = r
    cw = rndGrid(r, c)
    cnt = cwSum(cw)
    for w, n in zip(cw, cnt):
        print('\t', w, '\t', n)
    cw = newGen(cw)
    print(cw, '\n')

    cw = newGen(cw)
    print(cw, '\n')

    cw = newGen(cw)
    print(cw, '\n')

    cw = newGen(cw)
    print(cw, '\n')

    plt.matshow(cw)
    plt.show()

