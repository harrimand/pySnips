# Generate expressions for 4 bit digital comparator
import numpy as np
from qm import *

nbits = 5

def logisim(sop):
    """ Insert spaces between variables for Logisim compatibility"""
    return " ".join(list(sop)).replace('! ', '!').replace('  +  ', ' + ')

D = np.arange(2**(2 * nbits))

gt = [int(n) for n in list(np.where(D//(2**nbits) > D%(2**nbits))[0])]
lt = [int(n) for n in list(np.where(D//(2**nbits) < D%(2**nbits))[0])]
eq = [int(n) for n in list(np.where(D//(2**nbits) == D%(2**nbits))[0])]

print('\n\n', gt)
print('\n\n', lt)
print('\n\n', eq)

dc = []

Vars = [chr(n) for n in range(ord('A'), ord('A')+(2*nbits))]
print('\n\n')
print("Variables: ", Vars)

print("Input A: ", [chr(n) for n in range(65, 65 + nbits)])
print("Input B: ", [chr(n) for n in range(65 + nbits, 65 + 2 * nbits)])


gtSop = tt2ssop(gt, dc)
ltSop = tt2ssop(lt, dc)
eqSop = tt2ssop(eq, dc)

print('\n\ngt:\n', gtSop)
print('\n\nlt:\n', ltSop)
print('\n\neq:\n', eqSop)

print('\n\n')

with open('comp.txt', 'w') as cp:
    cp.write('gt:\n')
    cp.write(logisim(gtSop))
    cp.write('\n')
    cp.write('eq:\n')
    cp.write(logisim(eqSop))
    cp.write('\n')
    cp.write('lt:\n')
    cp.write(logisim(ltSop))

