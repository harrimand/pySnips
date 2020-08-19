
from logic.logic import *
from logic.lv import *

test = 4

if(test == 1):
    T = lv(4)
    print(T.tt)
    A, B, C, D = T.cols()
    print("\n", A)
    print("\n", B)
    print("\n", C)
    print("\n", D)

    x1 = XOR(A, C)
    x2 = XOR(B, D)
    x3 = AND(x1, x2)

    T.newCol([x1, x2, x3])

    Labels = ["A", "B", "C", "D", "$x1 = A \oplus C$", "$x2 = B \oplus D$", "$x1 \cdot x2$"]


    print("\t\t")
    for t in T.tt:
        print(t)

    T.logicPlot(Labels)
#---------------------------------------------------------------------------------------------

if(test == 2):
    T = lv(5)
    print(T.tt)
    A, B, C, D, E = T.cols()
    print("\n", A)
    print("\n", B)
    print("\n", C)
    print("\n", D)
    print("\n", E)

    x1 = XOR(B, D)
    x2 = XOR(C, E)
    x3 = AND(x1, x2)

    T.newCol([x1, x2, x3])

    Labels = ["A", "B", "C", "D", "E", "$x1 = B \oplus D$", "$x2 = C \oplus E$", "$x1 \cdot x2$"]

    print("\t\t")
    for t in T.tt:
        print(t)

    T.logicPlot(Labels)
#---------------------------------------------------------------------------------------------

if(test == 3):
    T = lv(5)
    A, B, C, D, E = T.cols()

    x1 = OR(AND(XNOR(A, B), D), AND(XOR(A, B), E))
    x2 = XOR(NOT(B), XNOR(C, E))
    x3 = AND(x1, x2)

    T.newCol([x1, x2, x3])

    Labels = ["A", "B", "C", "D", "E",
        "$x1 = \overline{A \oplus B} \cdot D + (A \oplus B) \cdot E$",
        "$x2 = \overline{B} \oplus \overline{C \oplus E}$",
        "$x1 \cdot x2$"]

    T.logicPlot(Labels)

#---------------------------------------------------------------------------------------------

if(test == 4):
    from logic.qm import *
    import numpy as np
    T = lv(5)
    A, B, C, D, E = T.cols()

    x1 = AND(AND(NOT(A), NOT(B)), C)
    x2 = AND(AND(NOT(A), B), D)
    x3 = AND(AND(A, NOT(B)), E)
    x4 = AND(A, B)
    X = OR(OR(OR(x1, x2), x3), x4) 

    T.newCol([x1, x2, x3, x4, X])

    Labels = ["A", "B", "C", "D", "E",
        "$x1 = \overline{A} \cdot \overline{B} \cdot C$",
        "$x2 = \overline{A} \cdot B, \cdot D$",
        "$x3 = A \cdot \overline{B} \cdot E$",
        "$x4 = A \cdot B$",
        "$x1 + x2 + x3 + x4$"]

    T.logicPlot(Labels)
    for t in T.Labels:
        print("\nLabels: \n", t)

    Ch = T.ax.get_children()

    print("\n\n")

    for ch in Ch:
        print(ch)

    outImps = [int(n) for n in np.where(np.array(X) == 1)[0]]
    print("\nOut Imps: ", outImps)

    sop = tt2ssop(outImps, [])
    print("\nSOP: ", sop)

#---------------------------------------------------------------------------------------------












