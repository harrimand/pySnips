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

kap = 5697
print("\t", kap)
while(kap != 6174):
    sti = str(kap)
    digits = [int(c) for c in sti]
    digsort = sorted(digits)
    fwd = int("".join([str(n) for n in digsort]))
    digrev = sorted(digits, reverse=True)
    rev = int("".join([str(n) for n in digrev]))
    kap = rev - fwd
    print("\t", kap)
