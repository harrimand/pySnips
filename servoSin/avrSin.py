
import math

pwMax = 2350
pwMin = 450
# travTime = 3.5
travTime = float(input("Enter Sweep Time: "))
print("\nSweep time is: ", travTime, " Seconds\n")

deltaT = .02
pwMid = (pwMax + pwMin) / 2
pwRange = pwMax - pwMid
steps = int(travTime / deltaT)

print("  Max:", pwMax, "  Min:", pwMin, "  Mid:", pwMid, "  Range:", pwRange, "  Steps:", steps, "\n")

data = []
for t in range(steps):
    pos = int(pwRange / 2 * math.sin(t * 2 * math.pi / steps) + pwMid)
    data.append(pos)

print(data)

#Generate list of step sizes that can be added to Pulse Width register
stepSize = []
stepSizeSigned = []
for i, d in enumerate(data):
    size = data[(i + 1)%len(data)] - d
    stepSize.append(size)
    stepSizeSigned.append(size if size >= 0 else 256 + size)

print("\nStep Size\n", stepSize)

# Generating a string containing all 8 bit signed hex values formatted as a table with .db (define byte)
# directives that can be included in the AVR program.

TaddLable = "TABLEaddr" + str(travTime).replace(".","_")
TendLable = "TABLEend" + str(travTime).replace(".","_")

Table = TaddLable + ":\n.db\t"
for i, s in enumerate(stepSizeSigned):
    Table += "$" + hex(s)[2:].zfill(2).upper()
    Table += "\n.db\t" if i % 8 == 7 and i < len(stepSizeSigned) - 1 else\
    "\n" if i >= len(stepSizeSigned) - 1 else ",\t"
Table += TendLable + ":"

print("\n\n", Table, "\n\n")
fileName = "sinTable" + str(travTime).replace('.','_')
print("\n\tWriting sin Table to " + fileName + "\n")

with open(fileName, 'w') as sT:
    sT.write("; " + str(travTime) + " Second Sweep Time \n")
    sT.write(Table)


