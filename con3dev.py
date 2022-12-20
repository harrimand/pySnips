
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# rot = [(p,r,c) for p in range(-1,2) for r in range(-1,2) for c in range(-1, 2)\
#  if (p+r+c)!=0]

rot = [(p,r,c) for p in [-1, 0, 1] for r in [-1, 0, 1] for c in [-1, 0, 1]\
        if any([p, r, c])]

# if not(p == 0 and r == 0 and c == 0)]

# nd(Rows, Columns, Pages) Create numpy 3D array filled
#     with sequence 0 -> (r * c * p - 1)
nd = lambda r, c, p: [[[(P*r*c)+(C+R*c) for C in range(c)] for R in range(r)]\
 for P in range(p)]


# Generate 3d array with random 0s and 1s
rand3d = lambda P, R, C: np.array([[[np.random.randint(2) for c in range(C)]\
 for r in range(0, R*C, C)] for p in range(0, R*C*P, R*C)])

c3 = rand3d(3, 4, 5)

def neighbors(c3):
    s = np.zeros_like(c3)
    for r in rot:
        s += np.roll(c3, (r[0],r[1],r[2]), (0, 1, 2))
    return s

def newgen():
    c3 = rand3d(3, 4, 5)
    nc = np.array(neighbors(c3))
    # print(nc)
    return nc

def genX(p, r, c):
    c3 = rand3d(p, r, c)
    nc = np.array(neighbors(c3))
    # print(nc)
    return (c3, nc)

ng = newgen()

cw, nc = genX(8, 8, 8)

gw = np.where(cw == 1)
ax.scatter(gw[0], gw[1], gw[2], c='black')
plt.show()


