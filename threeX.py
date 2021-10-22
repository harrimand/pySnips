
# https://interestingengineering.com/video/the-easiest-math-problem-no-one-can-solve

import sys

def threeX(m):
    ''' 3x+1 generator.
    If nList(n) is even nList[n+1] = nList[n] / 2
    else nList[n+1] = nList[n] * 3 + 1
    Generate new values until repeating sequence 4, 2, 1 is found.'''

    nList = []
    print(m, end = ' ')
    # while(m not in nList):
    while(m != 1):
        nList.append(m)
        if(m%2 == 0):
            m = int(m / 2)
        else:
            m = int(m * 3 + 1)
        print(m, end = ' ')
    print('\n')
    return nList

if __name__ == "__main__":
    thrX = []
    for n in sys.argv[1:]:
        thrX.append(threeX(int(n)))
#    print(thrX)

'''
thrXlenD = {}
for i, n in enumerate(thrXlen):
    thrXlenD[i] = n

thrXlenDs = dict(sorted(thrXlenD.items(),key= lambda x:x[1]))

thrXlenDs
'''



