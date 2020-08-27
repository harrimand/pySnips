

S = "AB!CD!E + !AB!C!DE + A!BCD!E"

t = "AB!CD!E + !AB!C!DE + A!BCD!E"

# u = "A!C!E + B!C!D + A!B!E"
u = "A!C!E + B!C + A!B!D"


trx = lambda *args: list(map(list, zip(*args)))
xor = lambda *args: [reduce(lambda a,b: a^b, R) for R in trx(*args)]


Vars = []
for V in u:
    if(ord(V) > 64 and ord(V) < 92 and V not in Vars):
        Vars.append(V)

uL = u.split(" + ")

Vars.sort()
print("\n\n\tVars: ", Vars)

uS = []
for U in uL:
    sS = ""
    for ch in Vars:
        if(ch not in U):
            sS = sS + '?'
        elif '!' + ch in U:
            sS = sS + '!' + ch
        else:
            sS = sS + ch
    uS.append(sS)

print('\n\n\tu: ', u)

print("\n\n\tsubStr: ", uS)

newuS = []
for T in uS:
    # print("\nTerm: ", T)
    Cnt = T.count('?')
    subBits = [list(bin(N)[2:].zfill(Cnt)) for N in range(2**Cnt)]
    # print("\nsubBits: ", subBits)
    termList = []
    for sB in subBits:
        # print("sB: ", sB)
        Tt = T
        for b in sB:
            Tt = Tt.replace('?', b, 1)
            # print(b, end=' ')
        # print("\n\nNew Term: ", T)
        termList.append(Tt)
    newuS = newuS + termList

print("\n\nnewuS: ", newuS)

binImps = []
for T in newuS:
    while('!' in T):
        iLoc = T.find('!')
        T = T.replace(T[iLoc:iLoc+2], '0')
    for t in T:
        if(t >= 'A' and t <= 'Z'):
            T = T.replace(t, '1')
    binImps.append(T)

print("\n\nbinImps: ", binImps)


D = sorted([int(B, 2) for B in binImps])


print("\n\nDecimal: ", D)




