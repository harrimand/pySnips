
#! /usr/bin/env python3
#
# subNet.py
# http://ascii-table.com/ansi-escape-sequences.php

import colorama # colorama required on Windows for font colors
colorama.init()

q = lambda n: int(bin(n)[2:],4)
qt = [[q(m) + 2 * q(n) for m in range(16)] for n in range(16)]

def drawVLSMtable(qt, ip, cidr):
    snAdd = ip & int(256 - 2**(32 - cidr))
    bcAdd = snAdd + 2**(32 - cidr) - 1
    for r in qt:
        print('\n')
        for c in r:
            if(c == ip):
                print("\033[33m{}\033[00m".format(str(c).rjust(5)),end='')
            elif (c >= snAdd and c <= bcAdd):
                print("\033[31m{}\033[00m".format(str(c).rjust(5)),end='')
            else:
                print(str(c).rjust(5), end='')

def drawNets(qt, nets):
    for r in qt:
        print('\n')
        for c in r:
            printed = False
            for net in nets:
                if(c >= net.sn and c <= net.bc):
                    print(net.col + "{}\033[00m".format(str(c).rjust(5)), end='')
                    printed = True
                    break
            if(not printed):
                print("\033[30m" + str(c).rjust(5) + "\033[00m", end='')


class subNet:
    def __init__(self, ip, cidr, color):
        self.cidr = cidr
        self.sn = ip & int(256 - 2**(32 - cidr))
        self.bc = self.sn + 2**(32-cidr)-1
        self.col = color

colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m"]

print("\nIP Address Entry:\n\tOption 1: nnn.nnn.nnn.nnn/hh\n\t\
Option 2: nnn/hh\n\tOption 3: nnn\n")

netNum = 0
net = []
runAgain = 'Y'
while(runAgain == '' or runAgain[0] == 'Y'):
    print("\033[1;2H\033[1K")
#    print("\033[2J")
    cidr = 0
    ip = -1
    while(ip < 0 or ip > 255):
        ipT = input("\nEnter IP Address: ")
        if("/" in ipT):
            cidr = int(ipT[ipT.rfind("/")+1:])
            ip = int(ipT[ipT.rfind('.')+1:ipT.rfind("/")])
        else:
            ip = int(ipT[ipT.rfind('.')+1:])

    while(cidr < 24 or cidr > 30):
        cidr = int(input("\nEnter CIDR 24..30 (Number of Subnet Mask bits): "))

    print("\033[2J")

    snAdd = ip & int(256 - 2**(32 - cidr))

    net.append(subNet(ip, cidr, colors[netNum % len(colors)]))

#    print("\nip: {}  cidr: {}".format(ip, cidr))
#    drawVLSMtable(qt, ip, cidr)

    sortN = sorted(net, key=lambda subnet: subnet.sn)

#    for sN in net:
#        print(sN.col + "\tSubNet: {}\t Broadcast: {}\033[00m\n".format(sN.sn, sN.bc))

    print("\n\n\tSubnets:\n")

    for sN in sortN:
        print(sN.col + "\tSubNet: {}/{}\t Broadcast: {}\033[00m\n".format(sN.sn, sN.cidr, sN.bc))

    netNum += 1

    drawNets(qt, sortN)

    runAgain = input("\n\nRun Again? [Y | N]: ").upper()
    print("\033[1A\033[1K                      ")

