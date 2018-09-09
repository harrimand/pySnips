#!/bin/bash/python3
# Module takes a list and prints the transposed list to columns
#    Parameters: List, Number of columns, column width
# Author:  Darrell Harriman harrimand@gmail.com
# Date:  9-9-2018
#
def printCols(data, cols, cw=10):
    """Print List items formatted into columns
        data: List of date to be printed.
        cols: Number of columns displayed.
        cw:   Column width (Default = 10 characters)"""

    print("\n    ", end="")
    for r in range(int(len(data)/cols+1)):
        for c in range(cols):
            try:
                index = r + int(len(data)/cols + 1) * c
                print(data[index], " " * (cw - len(str(data[index]))), end="")
            except IndexError:
                pass
        print("\n\n    ", end="") # End of row.  Start new row.

if __name__=="__main__":
    print("_"*60, "\n\n")
    # Example creating an ASCII Character Code Table
    alpha = [chr(n) for n in range(48, 123)] # Example contains printable characters
    ASCIItable = [n + " " + str(ord(n)) for n in alpha] # Appending character codes

    cols = 8    # select number of columns
    colWidth = 6  # Column Width (output padded with spaces)
    print("\n    ASCII Character Code table\n")
    printCols(ASCIItable, cols, colWidth)

#_______________________________________________________________________________

"""
OUTPUT:
____________________________________________________________

    ASCII Character Code table

    0 48   : 58   D 68   N 78   X 88   b 98   l 108  v 118  

    1 49   ; 59   E 69   O 79   Y 89   c 99   m 109  w 119  

    2 50   < 60   F 70   P 80   Z 90   d 100  n 110  x 120  

    3 51   = 61   G 71   Q 81   [ 91   e 101  o 111  y 121  

    4 52   > 62   H 72   R 82   \ 92   f 102  p 112  z 122  

    5 53   ? 63   I 73   S 83   ] 93   g 103  q 113  

    6 54   @ 64   J 74   T 84   ^ 94   h 104  r 114  

    7 55   A 65   K 75   U 85   _ 95   i 105  s 115  

    8 56   B 66   L 76   V 86   ` 96   j 106  t 116  

    9 57   C 67   M 77   W 87   a 97   k 107  u 117  

"""
