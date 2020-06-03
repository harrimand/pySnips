# matDev.py
# matrix operation functions

import numpy as np


arrIndex3D = lambda P, R, C: np.array([[[p + r + c for c in range(C)] for r in range(0, R*C, C)] for p in range(0, R*C*P, R*C)])


arrIndex2D = lambda R, C: np.array([[r + c for c in range(C)] for r in range(0, R*C, C)])


def minor(M, r, c): 
    """Return Minor matrix from M[r, c]
    Minor matrix contains all elements of M that are not in row 'r' or column'c'"""
    cols = np.concatenate((M[:,:c], M[:,c+1:]),axis=1)
    return np.concatenate((cols[:r,:], cols[r+1:,:]), axis=0)


def mSign(r, c): 
    """Return matrix of alternating checkered +1, -1 for us in Cramer's rule
    return matrix size [r, c]"""
    return np.array([[((R + C + 1) % 2)*2-1 for C in range(c)] for R in range(r)])

def matCofactors(M):
    """ Return M with alternate checkered cells negated my multiplying with -1 """
    r, c = np.shape(M)
    S = np.array([[((R + C + 1) % 2)*2-1 for C in range(c)] for R in range(r)])
    return np.multiply(M, S)

def matMinors(M):
    """Return matrix of minors for all elements in M"""
    m = np.zeros_like(M)
    for i, r in enumerate(M):
        for j, c in enumerate(r):
            m[i, j] = np.linalg.det(minor(M, i, j)) 
            # print(minor(M, i, j), "\n")
    return m

def printDet(M, rowCol, n): 
    """Generate strings showing Determinant calculations for selected Row or Column of M"""
    outStr = []
    Ms = matCofactors(M)
    rc = rowCol.upper()[0]
    if(rc == 'R'):
        for i in range(np.shape(M)[0]):
            m = minor(M, n, i)
            outStr.append(f" {Ms[n,i]} * ({m[0,0]} * {m[1,1]} - {m[1,0]} * {m[0,1]}) ")
    elif(rc == 'C'):
        for i in range(np.shape(M)[0]):
            m = minor(M, i, n)
            outStr.append(f" {Ms[i, n]} * ({m[0,0]} * {m[1,1]} - {m[1,0]} * {m[0,1]}) ")
    return outStr

# mTrx(M):  Transposes Matrix M
mTrx = lambda M: np.array([[M[r,c] for r in range(np.shape(M)[0])] for c in range(np.shape(M)[1])])

#----------------------------------------------------------------------------------------------------

tM = np.array([[3, 0, 2],[2, 0, -2],[0, 1, 1]])

print("Example finding inverse for 3x3 array tM:")
print("Array tM:\n", tM)
print("\n\n")


rcs = 'c' # r = row  c = column
rc = 2    # row or column number
detStr = printDet(tM, rcs, rc)
rowCol = "Row" if rcs.upper().startswith('R') else "Column"
print(f"Calculating Determinant with minors for {rowCol} {rc}\n")

for s in detStr:
    print(f"+ ({s})", end = ' ')
print("\n")

print("Determinant = ", end=' ')
Determinant = 0
for s in detStr:
    ev = eval(s)
    Determinant = Determinant + ev
    print(f"+ ({ev})", end = ' ')
print(f"= {Determinant}\n\n")


print("Minors: matMinors(tM)\n", matMinors(tM))
print("\n\n")

print("Signed Cofactors: matCofactors(matMinors(tM))\n", matCofactors(matMinors(tM)))
print("\n\n")

print("Transposed: mTrx(matCofactors(matMinors(tM)))\n", mTrx(matCofactors(matMinors(tM))))
print("\n\n")

print("Multiply Transposed Matrix of Cofactors of Minors by 1 / Determinant of Array\n")

print("Inverse Matrix:")
print("np.multiply(1 / Determinant, mTrx(matCofactors(matMinors(tM)))))\n")
tMinv = np.multiply(1 / Determinant, mTrx(matCofactors(matMinors(tM))))
print(tMinv)


print("\n\n")
print("Testing inverse with numpy: np.linalg.inv(tMinv)")
print(np.linalg.inv(tMinv))

print("\n\n")
print("Transposed\n", mTrx(tM))
print("\n\n")
