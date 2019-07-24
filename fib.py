#!/usr/bin/env python3

from os import sys

args = sys.argv[1:]

# print(float(args[0]) + float(args[1]))

def fibgen(n):
    f = [1, 1]
    for s in range(n - 2):
        f.append(f[s] + f[s+1])
    return f

def goldenRatio(series):
    gR = []
    for n in range(len(series) - 1):
        gR.append(series[n+1] / series[n])
    return gR

fibSeries = fibgen(int(args[0]))
print('\n', fibSeries, '\n')

ratio = goldenRatio(fibSeries)
print(ratio)
