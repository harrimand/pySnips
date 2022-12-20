#!/usr/bin/env python3.8

import numpy as np
# import timeit

roll2d = lambda M, r, c: np.roll(M, (-r, -c), axis=(0, 1))
'''
def conSum(M):
    sM = roll2d(M, 1, 1)
    sM = np.add(sM, roll2d(M, 1, 0))
    sM = np.add(sM, roll2d(M, 1, -1))
    sM = np.add(sM, roll2d(M, 0, -1))
    sM = np.add(sM, roll2d(M, -1, -1))
    sM = np.add(sM, roll2d(M, -1, 0))
    sM = np.add(sM, roll2d(M, -1, 1))
    sM = np.add(sM, roll2d(M, 0, 1))
    return sM
'''

# Optional function to rotate and add arrays.
rotSel = [[b1, b2] for b1 in range(-1,2) for b2 in range(-1, 2) if [b1, b2] != [0, 0]]
def conSum(M):
    Ms = np.zeros_like(M)
    for rs in rotSel:
        Ms = np.add(Ms, roll2d(M, rs[0], rs[1]))
    return Ms

arr3d = lambda P, R, C: np.array([[[p + r + c for c in range(C)] for r in range(0, R*C, C)] for p in range(0, R*C*P, R*C)])
rand3d = lambda P, R, C: np.array([[[np.random.randint(2) for c in range(C)] for r in range(0, R*C, C)] for p in range(0, R*C*P, R*C)])

c = np.array([[[p*100 + r*10 + c for c in range(1,5)] for r in range(1, 5)] for p in range(1, 5)])

def rnd3d(p, r, c);
    z = np.zeros((p,r,c)
    z[p, r, c] = np.randint(2) for P in range(p+1) for R in range(r+1) for C in range(c+1)
    return z





# Get 3D subArray wrapped
# saw(Matrix, page, row, column, pagesize, rowsize, colsize)
saw = lambda M, p, r, c, ps, rs, cs: np.roll(M, (-p, -r, -c), axis=(0, 1, 2))[:ps,:rs,:cs]

# Get count of neighbors in 3D array
def neighbor_Count3d(b):
    bs = np.zeros_like(b)
    for i, p in enumerate(b):
        for j, r in enumerate(p):
            for k, c in enumerate(r):
                cu333 = np.roll(b, (-i+1, -j+1, -k+1), axis=(0, 1, 2))[:3, :3,:3]
                bs[i,j,k] = np.sum(cu333) - cu333[1, 1, 1]
    return bs


rd = np.array([[p, r, s] for s in range(-1,2) for r in range(-1,2) for p in range(-1,2) if not [p, r, s] == [0, 0, 0]])
def nCount(o3):
    os = np.zeros_like(o3)
    for r in rd:
        os = np.add(os, np.roll(o3, r, axis=(0,1,2)))
    return os



def sum3d(M):
    sM = np.zeros_like(M)
    rotSel = np.array([[b1, b2, b3] for b1 in range(-1,2) for b2 in range(-1, 2) for b3 in range(-1, 2)
            if [b1, b2, b3] != [0, 0, 0]])
    for s in rotSel:
        sM = np.sum(np.roll(M, (rotSel[s][0], rotSel[s][1], rotSel[s][2]), (0, 1, 2)))
    return sM


n = rand3d(3, 3, 3)
sA = lambda b: np.zeros(np.add(np.array(np.shape(b)), np.array([2, 2, 2])))
nS = sA(n)
nS[1:-1, 1:-1, 1:-1] = n

nS[0,1:-1,1:-1] = n[-1]      # nS[p0] = n[p-1]
nS[-1,1:-1,1:-1] = n[0]      # nS[p-1] = n[p0]

nS[1:-1,0,1:-1] = n[:,-1,:]
nS[1:-1,-1,1:-1] = n[:,0,:]

nS[1:-1,1:-1,0] = n[:,:,-1]
nS[1:-1,1:-1,-1] = n[:,:,0]

nS[1:-1,1:-1,0] = n[:,:,-1]
nS[1:-1,1:-1,-1] = n[:,:,0]

nS[0, 0, 1:-1] = n[-1,-1,:]
nS[0,-1, 1:-1] = n[-1, 0, :]

nS[-1, 0, 1:-1] = n[0,-1,:]
nS[-1,-1, 1:-1] = n[0, 0, :]

nS[1:-1, 0, 0] = n[:,-1,-1]
nS[1:-1, 0, -1] = n[:, -1, 0]

nS[1:-1, -1, 0] = n[:, 0, -1]
nS[1:-1, -1, -1] = n[:, 0, 0]




# Msum = np.zeros_like(M)
# Msum = [np.add(Msum, roll2d(M, r[0], r[1])) for r in rotSel]

def newGen(M, sM):
    newM = np.array(((sM > 2) & (sM < 5) & M) | ((sM==3) & (M==0)), dtype=int)
    return newM

# RC = np.array([[r*10+c for c in range(1, 10)] for r in range(1, 10)])

rows=24
cols=24

G = np.array([[np.random.randint(2) for _ in range(rows)] for _ in range(cols)])

# print(G)

# print('\n')

# print(roll2d(G, 1, 1))

# cS = conSum(G)

# print(cS)

print('\n')

# print(newGen(G, cS))

print(G)
print('\n')

for n in range(5):
#    startTime = timeit.default_timer()
    G = newGen(G, conSum(G))
#    T = timeit.default_timer() - startTime
#    print('\tTime: ', T, '  Freq: ', 1/T)
    print(G)
    print('\n')



