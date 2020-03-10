
from os import sys

#-------------------------------------------------------------------
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

#-------------------------------------------------------------------
# Getting user input from command line
if len(sys.argv) > 1:
	n = int(sys.argv[1])
else:
	print('\nNo User Input!  Using test number.')
	n = 1366776851540808708000000
#	n = 4620523908000000
#	n = 4620523908E6

#-------------------------------------------------------------------
# Calling function to find prime factors
n = int(n)
PF = prime_factors(n)
print('\n\n', PF, '\n')

#-------------------------------------------------------------------
# Formatting list for displaying results
UF = set(PF)	# Unique set of factors
CF = []			# List for exponential notation
for U in UF:
	if PF.count(U) > 1:
		CF.append(str(U) + '^' + str(PF.count(U)))
	else:
		CF.append(str(U))

#-------------------------------------------------------------------
# Printing results
print('\n\t', n, ' = ', ' * '.join(CF), '\n')


# 1366776851540808708000000


