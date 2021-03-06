# vlsmm2.py

q = lambda n: int(bin(n)[2:],4)
ql = [q(n) for n in range(16)]

qt = [[ql[m] + 2 * ql[n] for m in range(16)] for n in range(16)]

with open('vlsm.txt', 'w') as fid:
    for r in qt:
        print('\n')
        fid.write('\n\n')
        for c in r:
            print(str(c).rjust(5), end='')
            fid.write(str(c).rjust(5))

def findRowCol(qt, ip):
    for r, ql in enumerate(qt):
        c = -1
        if(ip in ql):
            c = ql.index(ip)
            break
    return [r, c]

def dispSN(qt, ip, cidr):
    snAdd = ip & int(256 - 2**(32 - cidr))
    bcAdd = snAdd + 2**(32 - cidr) - 1
    snRC = findRowCol(qt, snAdd)
    bcRC = findRowCol(qt, bcAdd)
    for r in qt[snRC[0]:bcRC[0]+1]:
        print('\n')
        for c in r[snRC[1]:bcRC[1]+1]:
            print(str(c).rjust(5), end='')
    print('\n\n')

runAgain = 'Y'
while(runAgain[0] == 'Y'):
    ip = -1
    while(ip < 0 or ip > 255):
        ipT = input("\n\nEnter IP Address: ")
        ip = int(ipT[ipT.rfind('.')+1:])

    cidr = 0
    while(cidr < 24 or cidr > 30):
        cidr = int(input("\nEnter CIDR (Number of Subnet Mask bits): "))
        snAdd = ip & int(256 - 2**(32 - cidr))

    for r, ql in enumerate(qt):
        c = -1
        if(ip in ql):
            c = ql.index(ip)
            break

    print("\nipAdd: {}  IP Row: {}\tColumn: {}\n".format(ip, r, c))

    snRC = findRowCol(qt, snAdd)
    print("snAdd: {}  SN Row: {}\tColumn: {}\n".format(snAdd, snRC[0], snRC[1]))

    bcAdd = snAdd + 2**(32 - cidr) - 1
    bcRC = findRowCol(qt, bcAdd )
    print("bcAdd: {}  BC Row: {}\tColumn: {}\n".format(bcAdd, bcRC[0], bcRC[1]))

    dispSN(qt, ip, cidr)
    runAgain = input("\nRun Again? [Y | N]: ").upper()

