
from logic import *
from km import *
from lv import *
from qm import *

T = lv(4)
A, B, C, D = T.cols()


Q1b = OR(XNOR(A, C), XNOR(B, C))
Q2b = OR(XNOR(A, B), XNOR(B, C))

T.newCol([Q1b, Q2b])

Q1imps = [int(n) for n in np.where(np.array(Q1b) == 1)[0]]
Q2imps = [int(n) for n in np.where(np.array(Q2b) == 1)[0]]

print("Q1 Truth Table: ", Q1imps)
print("Q2 Truth Table: ", Q2imps)

Q1str = karnaughMap(Q1imps, 10)
Q2str = karnaughMap(Q2imps, 10)

Q1usop = tt2usop(Q1imps)
Q1ssop = tt2ssop(Q1imps, [])

Q2usop = tt2usop(Q2imps)
Q2ssop = tt2ssop(Q2imps, [])



for k, m in zip(Q1str, Q2str):
    print(k, m)

print("\n\n")

print("Q1 Unsimplified SOP: ", Q1usop)
print("Q1 Simplified SOP: ", Q1ssop)
print("\n")
print("Q2 Unsimplified SOP: ", Q2usop)
print("Q2 Simplified SOP: ", Q2ssop)
print("\n\n")

Labels = ["A", "B", "C", "D",
    "$Q1 = \overline{A\;\oplus\;C}\;+\;\overline{B\;\oplus\;C}$",
    "$Q2 = \overline{A\;\oplus\;B}\;+\;\overline{B\;\oplus\;C}$"]

T.logicPlot(Labels)



