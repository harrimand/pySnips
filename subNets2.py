#! /usr/bin/env python3
#
# subNet.py
# http://ascii-table.com/ansi-escape-sequences.php

import colorama # colorama required on Windows for font colors
colorama.init()

q = lambda n: int(bin(n)[2:],4)
qt = [[q(m) + 2 * q(n) for m in range(16)] for n in range(16)]

'''
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
'''

def drawNets(qt, nets):
    print("\033[1;1H")
    print("\n"*10)
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
        self.name = " "

def menu():
    menuOpt = 'X'
    print("\033[1;1H")
    print("\n\n\n\033[37m" + "Add subnet [A]".rjust(20) + "\033[00m")
    print("\033[37m" + "Delete subnet [D]".rjust(20) + "\033[00m")
    print("\033[37m" + "Reset subnets [R]".rjust(20) + "\033[00m")
    print("\033[37m" + "Name subnet [N]".rjust(20) + "\033[00m")
    print("\033[37m" + "Quit [Q]".rjust(20) + "\033[00m")
    while(not(menuOpt in ['A', 'D', 'R', 'N', 'Q'])):
        menuOpt = input("Choose Option: ").upper()
        print("\033[1A" + " "*30)
        if (menuOpt == ''):
            menuOpt = 'A'
        print("\033[1A\033[15C   \033[1A\033[3D")
    return menuOpt

def addSubNet(net, netNum):
    ip = -1
    cidr = 0
    colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m"]
    while(ip < 0 or ip > 255):
        print("\033[1;1H")
        ipT = input("\n"*9 + "Enter IP Address: ")
        print("\033[1A" + " "*30)
        if("/" in ipT):
            cidr = int(ipT[ipT.rfind("/")+1:])
            ip = int(ipT[ipT.rfind('.')+1:ipT.rfind("/")])
        elif(ipT == ''):
            ip = -1
        else:
            ip = int(ipT[ipT.rfind('.')+1:])

    while(cidr < 24 or cidr > 30):
        cidr = int(input("\nEnter CIDR 24..30 (Number of Subnet Mask bits): "))

    snAdd = ip & int(256 - 2**(32 - cidr))
    net.append(subNet(ip, cidr, colors[netNum % len(colors)]))

def delSubNet(net, sortN):
    print("\033[1;1H")
    id = int(input("\n"*9 + "Select Subnet to Delete: "))
    print("\033[1A" + " "*30)
    net.remove(sortN[id])
    del sortN[id]

def nameSubNet(sortN):
    print("\033[1;1H")
    id = int(input("\n"*9 + "Select Subnet to Name: "))
    Name = input("Enter Name: ")
    sortN[id].name = Name
    print("\033[1A" + " "*30)
    print("\033[2A" + " "*30)

colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m"]

print("\033[1J\033[37m" + "Subnet Viewer".rjust(50))
print("\033[1;10H..." + "\n"*10)
sortN = [subNet(0, 24, "\033[30m")]
print("\n" * 13)
drawNets(qt, sortN)
# print("\033[15A")
print("\033[1;1H..")
menuOpt = menu()

netNum = 0
net = []
runAgain = 'A'
while(menuOpt != 'Q'):
    if(menuOpt == 'A'):
        addSubNet(net, netNum)
        sortN = sorted(net, key=lambda subnet: subnet.sn)
        netNum += 1
    elif(menuOpt == 'D'):
        delSubNet(net, sortN)
        print("\n" * (36 + len(sortN) * 2) + " " * 60 + "-")
    elif(menuOpt == 'N'):
        print("\n"*40 + "N Selected")
        nameSubNet(sortN)
    else:
        netNum = 0
        netlen = len(net)
        net = []
        sortN = [subNet(0, 24, "\033[30m")]
        print("\033[0K              \033[1J\033[3;0H")
#        print("\033[1K***\033[3;0H")
        drawNets(qt, sortN)
        sortN = []
        print("\n\n")
        for L in range(netlen):
            print(" " * 60 + "\n")
#        print("\n"*40 + "R Selected")
    print("\033[1;10H..." + "\n"*10)
    drawNets(qt, sortN)
    print("\n\n")
    for n, sN in enumerate(sortN):
        print(sN.col + "   SubNet {}:  {}/{}  \t Broadcast: {}   \t{} \033[00m\n".format(n, sN.sn, sN.cidr, sN.bc, sN.name))

    print("\033[0;0H")
    menuOpt = menu()



'''
print("\nIP Address Entry:\n\tOption 1: nnn.nnn.nnn.nnn/hh\n\t\
Option 2: nnn/hh\n\tOption 3: nnn\n")

netNum = 0
net = []
runAgain = 'A'
while(runAgain == '' or runAgain[0] == 'A'):
    print("\033[1;2H\033[1K")
#    print("\033[2J")
    cidr = 0
    ip = -1
    while(ip < 0 or ip > 255):
        ipT = input("\nEnter IP Address: ")
        if("/" in ipT):
            cidr = int(ipT[ipT.rfind("/")+1:])
            ip = int(ipT[ipT.rfind('.')+1:ipT.rfind("/")])
        elif(ipT == ''):
            ip = -1
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

    for n, sN in enumerate(sortN):
        print(sN.col + "   SubNet {}: {}/{}\t Broadcast: {}\033[00m\n".format(n, sN.sn, sN.cidr, sN.bc))

    netNum += 1

    drawNets(qt, sortN)

    runAgain = menu()

#    runAgain = input("\n\nRun Again? [Y | N] or Reset[R]: ").upper()
    if(not(runAgain == '') and runAgain[0] == 'R'):
        netNum = 0
        net = []
        sortN = [subNet(0, 24, "\033[30m")]
        print("\033[0K              \033[1J\033[3;0H")
#        print("\033[1K***\033[3;0H")
        drawNets(qt, sortN)
        runAgain = 'A'
    print("\033[0A\033[1K                                   ")
'''
