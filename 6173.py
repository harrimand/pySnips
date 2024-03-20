# Kaprekar's Constant
''' Kaprekar's constant 6134
Choose a random 4 digit numbers with at least 2 different digits.
Sort digits decending order.
subtract number with digits in ascending order.
 Eg:  for 8273
    8732
   -2378
   -----
    6354
-----------------
    6543
   -3456
   -----
    3087

Repeat until answer is 6174
'''

inVal = 8732
sti = str(inVal)
stl = [int(c) for c in sti]
stlr = sorted(stl, reverse=True)
nr = int("".join([str(n) for n in stlr]))
n = sorted(stl)
res = nr = n



