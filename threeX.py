
# https://interestingengineering.com/video/the-easiest-math-problem-no-one-can-solve

import sys

from os import system

cls = lambda: system("clear")

def threeX(m, p=0):
    ''' 3x+1 generator.
    If nList(n) is even nList[n+1] = nList[n] / 2
    else nList[n+1] = nList[n] * 3 + 1
    Generate new values until repeating sequence 4, 2, 1 is found.'''

    nList = []
    if(p): print(m, end = ' ')

    # while(m not in nList):
    while(m != 1):
        nList.append(m)
        if(m%2 == 0):
            m = int(m / 2)
        else:
            m = int(m * 3 + 1)
    if(p): print(m, end = ' ')
    nList.append(1)
    print('\n')
    return nList

def parseRange(rStr):
    if(':' in rStr):
        return [int(s) for s in rStr.replace(' ', '').split(':')]
    else:
        return int(rStr.replace(' ', ''))

nx = lambda x: x * 2 if(((x-1)/3)%1 != 0) else (x - 1) / 3

nxL = [1, 2, 4, 8]
for n in range(40):
    nxL.append(int(nx(nxL[-1])))


if __name__ == "__main__":
    thrX = []
    for n in sys.argv[1:]:
        thrX.append(threeX(int(n), 1))
    print(thrX)


# eqX = len([1 if(ex[-i] == fx[-i]) for i in range(1,min(len(ex), len(fx)))])
# eqX = len([1 for i in range(1,min(len(ex), len(fx)))if(ex[-i] == fx[-i])])

cmpXY = lambda ex, fx: len([x for x, y in zip(ex[-1::-1], fx[-1::-1]) if x == y])

LX = [len(threeX(n)) for n in range(1,100)]
LXD = {n: len(threeX(n)) for n in range(1,100)}
LXd = {i:k for i, k in enumerate(LX)}
LXds = dict(sorted(LXD.items(), key=lambda x:x[1]))

'''
if __name__ == "__main__":
    ui =  int(input("\n\tPick a starting number: "))
    threeX(ui, 1)
'''




'''
thrxLen = [len(threeX(n)) for n in range(1, 100)]

thrXlenD = {}
for i, n in enumerate(thrXlen):
    thrXlenD[i] = n

thrXlenDs = dict(sorted(thrXlenD.items(),key= lambda x:x[1]))

thrXlenDs
'''


