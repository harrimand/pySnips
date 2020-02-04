import numpy as np
import qm
import matplotlib.pyplot as plt

def setWindowPos():
    F = plt.gcf()
    Size = F.get_size_inches()
    F.set_size_inches(Size[0]*6, Size[1]*3, forward=True)
    plt.show()

# imps = qm.impStr2impList("..3 7..11 14..16 24..28 30..")
# imps = qm.impStr2impList("..2 9..13 15..19 26..28 30..")
# imps = qm.impStr2impList("1..5 7 9..13 15 17..21 23 25..29")
# imps = qm.impStr2impList("0 1 2 4 5 7 9 10 12 13 15 17 18 20 21 23 25 26 28 29")
# imps = qm.impStr2impList("1 2 3 5 7 9 10 11 13 15 17 18 19 21 23 25 26 27 29 31")
# imps = qm.impStr2impList("1 2 5 6 9 10 13 14 16 17 20 21 24 25 28 29")
imps = qm.impStr2impList("0 2 3 5 6 7 9 10 11 12 14 15 16 17 18 20 21 22 23 24 25 27 28 29 30 31")



bitsIn = max(imps).bit_length()
tmax = 2**(bitsIn)

ttIndex = np.array([n for n in range(tmax)])

tt = np.array([1 if n in imps else 0 for n in range(tmax)]).T
# tt = [1 if n in imps else 0 for n in range(tmax)]

Tcount = np.array([[int(b) for b in bin(n)[2:].zfill(5)] for n in range(tmax)]).T

print("\nTruth Table Binary Input:\n")

for r in Tcount:
    print(r)

ssop = qm.tt2ssop(imps, [])

print("\n\nSimplified Sum of Products: ", ssop, '\n')

print("\nTruth Table:\n", tt, '\n')

tt_Tcount = np.append(Tcount, [tt], axis=0)

print("\nAppended Tables:\n")
for r in tt_Tcount:
    print(r)

sigs = tt_Tcount * .8

for y, r in enumerate(sigs[::-1][:]):
    plt.bar(ttIndex, r, bottom=y-1, width=1, align='edge')

print('\n\n')

plt.ylim(-1, bitsIn)
plt.xticks(ttIndex)
plt.yticks([n-1 for n in range(bitsIn+2)])
plt.grid()
plt.title('Q = ' + ssop, fontsize=20, fontweight='bold')

for V in range(bitsIn):
	C = chr(V + 65)
	plt.text(-.5, bitsIn - .6 - V, C, fontsize=30, fontweight='bold', ha='center', va='center')
plt.text(-.5, bitsIn - 1.6 - V, 'Q', fontsize=30, fontweight='bold', ha='center', va='center')

setWindowPos()


