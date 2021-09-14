
import numpy as np
from pandas import DataFrame as dF

from os import system
cls = lambda: system("clear")

# A = [['a', 'c', 'e'], ['g', 'i', 'k'], ['m', 'o', 'q'], ['s', 'u', 'w']]
# B = [['b', 'd', 'f'], ['h', 'j', 'l'], ['n', 'p', 'r'], ['t', 'v', 'x']]

alpha = [chr(n) for n in range(97, 121)]

A = np.reshape(alpha[::2], (3, 4))
B = np.reshape(alpha[1::2], (3, 4))

Z = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]

ABC = np.array([list("".join(a)) for a in Z])

print('\n\nA = \n', A)
print('\n\nB = \n', B)
print('\n\nZ = \n', Z)
print('\n\nAB = \n', ABC, '\n\n')

print('-'*80, '\n\n')

jKCols = ['J3', 'K3', 'J2', 'K2', 'J1', 'K1', 'J0', 'K0']


ABCdF = dF(ABC, index=['0', '1', '3'], columns = jkCols)

print(ABCdF)



