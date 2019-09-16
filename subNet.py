#! /usr/bin/env python3
# subNet.py

q = lambda n: int(bin(n)[2:],4)
qt = [[q(m) + 2 * q(n) for m in range(16)] for n in range(16)]

def drawVLSMtable(qt, ip, cidr):
    snAdd = ip & int(256 - 2**(32 - cidr))
    bcAdd = snAdd + 2**(32 - cidr) - 1
    for r in qt:
        print('\n')
        for c in r:
            if(c == ip):
                print("\033[93m{}\033[00m".format(str(c).rjust(5)),end='')
            elif (c >= snAdd and c <= bcAdd):
                print("\033[91m{}\033[00m".format(str(c).rjust(5)),end='')
            else:
                print(str(c).rjust(5), end='')

print("\nIP Address Entry:\n\tOption 1: nnn.nnn.nnn.nnn/hh\n\t\
Option 2: nnn/hh\n\tOption 3: nnn\n")

runAgain = 'Y'
while(runAgain[0] == 'Y'):
    cidr = 0
    ip = -1
    while(ip < 0 or ip > 255):
        ipT = input("\n\nEnter IP Address: ")
        if("/" in ipT):
            cidr = int(ipT[ipT.rfind("/")+1:])
            ip = int(ipT[ipT.rfind('.')+1:ipT.rfind("/")])
        else:
            ip = int(ipT[ipT.rfind('.')+1:])

    while(cidr < 24 or cidr > 30):
        cidr = int(input("\nEnter CIDR 24..30 (Number of Subnet Mask bits): "))
        snAdd = ip & int(256 - 2**(32 - cidr))

    print("\nip: {}  cidr: {}".format(ip, cidr))
    drawVLSMtable(qt, ip, cidr)

    runAgain = input("\n\nRun Again? [Y | N]: ").upper()

