
# 4 digit decimal to Cistercian number
# https://hackaday.io/project/178131-monklock 
# https://en.wikipedia.org/wiki/Cistercian_numerals


from os import system
import numpy as np
from time import strftime

cls = lambda: system("clear")

# px =   [[[0, 0],[0, 0],[0, 0]],[[1, 1],[0, 0],[0, 0]],
#         [[0, 0],[0, 0],[1, 1]],[[0, 0],[1, 0],[0, 1]],
#         [[0, 1],[1, 0],[0, 0]],[[1, 1],[1, 0],[0, 0]],
#         [[0, 1],[0, 1],[0, 1]],[[1, 1],[0, 1],[0, 1]],
#         [[0, 1],[0, 1],[1, 1]],[[1, 1],[0, 1],[1, 1]]]

# pc1x=   [[[' ', ' '],[' ', ' '],[' ', ' ']],[['0', '0'],[' ', ' '],[' ', ' ']],
#         [[' ', ' '],[' ', ' '],['0', '0']],[[' ', ' '],['0', ' '],[' ', '0']],
#         [[' ', '0'],['0', ' '],[' ', ' ']],[['0', '0'],['0', ' '],[' ', ' ']],
#         [[' ', '0'],[' ', '0'],[' ', '0']],[['0', '0'],[' ', '0'],[' ', '0']],
#         [[' ', '0'],[' ', '0'],['0', '0']],[['0', '0'],[' ', '0'],['0', '0']]]

pc1=   [[[' ', ' '],[' ', ' '],[' ', ' ']],[['o', 'o'],[' ', ' '],[' ', ' ']],
        [[' ', ' '],[' ', ' '],['o', 'o']],[[' ', ' '],['o', ' '],[' ', 'o']],
        [[' ', 'o'],['o', ' '],[' ', ' ']],[['o', 'o'],['o', ' '],[' ', ' ']],
        [[' ', 'o'],[' ', 'o'],[' ', 'o']],[['o', 'o'],[' ', 'o'],[' ', 'o']],
        [[' ', 'o'],[' ', 'o'],['o', 'o']],[['o', 'o'],[' ', 'o'],['o', 'o']]]

pc10 = [[[n[1], n[0]] for n in M] for M in pc1]
pc100 = [[n for n in [M[2],M[1],M[0]]] for M in pc1]
pc1000 = [[[n[1], n[0]] for n in M] for M in pc100]

# Display ones from 0 to 9
def dspNum_1(pc):
    for i, d in enumerate(pc):
        print('\t', i)
        for r in d:
            print('\t\to', r[0], r[1])
        print('\t\to')
        print('\t\to')
        print('\t\to')
        print('\t\to')

# Display tens from 10 to 90
def dspNum_10(pc):
    for i, d in enumerate(pc):
        print('\t', i*10)
        for r in d:
            print('\t\t', r[0], r[1], 'o')
        print('\t\t', ' ', ' ', 'o')
        print('\t\t', ' ', ' ', 'o')
        print('\t\t', ' ', ' ', 'o')
        print('\t\t', ' ', ' ', 'o')

# Display hundreds from 100 to 900
def dspNum_100(pc):
    for i, d in enumerate(pc):
        print('\t', i*100)
        print('\t\to')
        print('\t\to')
        print('\t\to')
        print('\t\to')
        for r in d:
            print('\t\to', r[0], r[1])

# Display thousands from 1000 to 9000
def dspNum_1000(pc):
    for i, d in enumerate(pc):
        print('\t', i*1000)
        print('\t\t', ' ', ' ', 'o')
        print('\t\t', ' ', ' ', 'o')
        print('\t\t', ' ', ' ', 'o')
        print('\t\t', ' ', ' ', 'o')
        for r in d:
            print('\t\t', r[0], r[1], 'o')

# dspNum_1000(pc1000)
# dspNum_100(pc100)
# dspNum_10(pc10)
# dspNum_1(pc1)

# print('\n\n')

def cistChar(N):
    ''' Create 5x7 matrix for 4 digit Cistercian number'''
    th = int(str(N).zfill(4)[0])
    hu = int(str(N).zfill(4)[1])
    te = int(str(N).zfill(4)[2])
    on = int(str(N).zfill(4)[3])

    pcf = [[' ', ' ']]
    pcc = [['o'],['o'],['o'],['o'],['o'],['o'],['o']]

    pcr = np.vstack((pc1[on],pcf, pc100[hu]))
    pcl = np.vstack((pc10[te],pcf, pc1000[th]))
    pch = np.hstack((pcl, pcc, pcr))
    return pch

def dspCist(N):
    ''' Display decimal number from 0 to 9999 in Cistercian
    number format on a 5x7 matrix.'''
    assert(N <= 9999 and N >= 0), "Number out of range"
    print('\n\t')
    cist = cistChar(N)
    for r in cist:
        print('\t', end='')
        for ch in r:
            print(ch, end=' ')
        print('')
    print('\n\n')

def timeDate():
    ''' Display 3 Cistercian numbers representing 24 hour time
    Hour and Minute hhmm, Month and Day MMDD, and Year YYYY'''
    td = [int(t) for t in strftime("%H %M %m %d %Y").split()]
    hm = cistChar(td[0] * 100 + td[1])
    md = cistChar(td[2] * 100 + td[3])
    yy = cistChar(td[4])

    spc = [[' '],[' '],[' '],[' '],[' '],[' '],[' ']]
    disp = np.hstack((hm, spc, spc, md, spc, spc, yy))
    print('\n')
    for r in disp:
        print('\t', end='')
        for ch in r:
            print(ch, end=' ')
        print('')
    print('\n\n')

print("\ttimeDate()  : Show current time hhmm, MMDD, YYYY\n\
    \tdspCist(N)  : Display 4 digit number in Cistercian formap\n\
    \tcistChar(N) : Create 5x7 Matrix representing Cistercian number\n")

timeDate()



