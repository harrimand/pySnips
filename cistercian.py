
#! /usr/bin/env python

# 4 digit decimal to Cistercian number
# https://hackaday.io/project/178131-monklock 
# https://en.wikipedia.org/wiki/Cistercian_numerals

from os import system
import numpy as np
from time import strftime

cls = lambda: system("cls")

pc1=   [[[' ', ' '],[' ', ' '],[' ', ' ']],[['o', 'o'],[' ', ' '],[' ', ' ']],
        [[' ', ' '],[' ', ' '],['o', 'o']],[[' ', ' '],['o', ' '],[' ', 'o']],
        [[' ', 'o'],['o', ' '],[' ', ' ']],[['o', 'o'],['o', ' '],[' ', ' ']],
        [[' ', 'o'],[' ', 'o'],[' ', 'o']],[['o', 'o'],[' ', 'o'],[' ', 'o']],
        [[' ', 'o'],[' ', 'o'],['o', 'o']],[['o', 'o'],[' ', 'o'],['o', 'o']]]

pc10 = [[[n[1], n[0]] for n in M] for M in pc1]
pc100 = [[n for n in [M[2],M[1],M[0]]] for M in pc1]
pc1000 = [[[n[1], n[0]] for n in M] for M in pc100]

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
    pc = np.hstack((pcl, pcc, pcr))
    return pc

def cistChars(M):
    ''' Read list of 4 digit integers.   Horizontally stack multiple 5x7
     matrices to display multiple Cistercian numbers'''
    spc = [[' '],[' '],[' '],[' '],[' '],[' '],[' ']]
    # disp = cistChar(M[0])
    disp = spc
    for i, N in enumerate(M):
        if(i < (len(M))):
            disp = np.hstack((disp, spc, spc))
        disp = np.hstack((disp, cistChar(N)))
    disp = np.hstack((disp, spc))
    return disp

def printMat(mat):
    print('\n')
    for r in mat:
        print('\t', end='')
        for ch in r:
            print(ch, end=' ')
        print('')
    print('\n')

def dspCist(N):
    ''' Display decimal number from 0 to 9999 in Cistercian
    number format on a 5x7 matrix.'''
    assert(N <= 9999 and N >= 0), "Number out of range"
    print('\n\t')
    cist = cistChar(N)
    printMat(cist)

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
    printMat(disp)
#     return disp

if __name__ == "__main__":
    timeDate()
else:
    print("\ttimeDate()  : Show current time hhmm, MMDD, YYYY\n\
        \tdspCist(N)  : Display 4 digit number in Cistercian formap\n\
        \tcistChar(N) : Create 5x7 Matrix representing Cistercian number\n")
