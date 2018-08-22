
from rpn import rpn
import sys

if len(sys.argv) > 1:
    R = rpn(" ".join([str(i) for i in sys.argv[1:]]))
else:
    R = rpn()

run = True

while run:
    Rin = input("RPN Entry: ")
    if Rin.startswith("ex"):
        run = False
    else:
        R.update(Rin)


