#!/bin/python3
"""Substituting strings found in file with strings in a dictionary.
File strings to be replaced are encapsulated with '{' and '}'.
Function searches for dictionary keys in string.  If matcthing
strings are encapsulated, it will replace them with values from
the dictionary."""

def subStrings(sT, subs):
    while '{ ' in sT:
        sT = sT.replace('{ ', '{')
    while ' }' in sT:
        sT = sT.replace(' }', '}')
    for key in subs.keys():
        sT = sT.replace('{'+key+'}', subs[key])
    return sT

subs = {'one': 'ONE', 'two': "TWO", 'three': 'THREE', 'four': 'FOUR'}

print('"""')
with open('testFile', 'r') as tF:
# Printing Input File
    print('_' * 40, "\n# Input File Name = testFile\n")
    for line in tF:
        print(line, end='')
    tF.seek(0)  #Reset file pointer to 0

# Printing Output after string replacements
    print('_' * 40, "\n# Output Text\n")
    for line in tF:
        print(subStrings(line, subs), end='')

print('_' * 60)
print('"""\n')

# Vim Command to write program output below cursor in this file:
# :r !python3 %

