
import numpy as np
from arr3d import *

M = rand3d(3, 3, 3)
N = rand3d(3, 3, 3)

O = np.array(np.logical_xor(M, N), dtype=int)

print(M[0,0,:], N[0,0,:], O[0,0,:] )
print(M[0,1,:], N[0,1,:], O[0,1,:] )
print(M[0,2,:], N[0,2,:], O[0,2,:] )

print('\n\n')

print(M[1,0,:], N[1,0,:], O[1,0,:] )
print(M[1,1,:], N[1,1,:], O[1,1,:] )
print(M[1,2,:], N[1,2,:], O[1,2,:] )

print('\n\n')

print(M[2,0,:], N[2,0,:], O[2,0,:] )
print(M[2,1,:], N[2,1,:], O[2,1,:] )
print(M[2,2,:], N[2,2,:], O[2,2,:] )

print('\n\n')

