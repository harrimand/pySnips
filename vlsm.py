
q = lambda n: int(bin(n)[2:],4)
vlsm = [[q(m) + 2 * q(n) for m in range(16)] for n in range(16)]

with open("vlsm.txt", 'w') as fid:
    for r in vlsm:
        print("\n")
        fid.write("\n\n")
        for c in r:
            print(str(c).rjust(5), end='')
            fid.write(str(c).rjust(5))
    fid.write("\n\n")
print("\n\n")

ipInt = -1
while(ipInt < 0 or ipInt > 255):
    ip = input("Enter IP Address: ")
    ipInt = int(ip[ip.rfind('.')+1:])
    print("\n")

cidr = 0
while(cidr < 24 or cidr > 30):
    cidr = int(input("Mask bit length (cidr) 24 <= length <= 30: "))
    msk = 256 - 2**(32 - cidr)
    print("\n")

ipNetOcts = ip[:ip.rfind('.')+1]

print("IP input last octet = {}\n".format(ipInt))
print("cidr input = {}\n".format(cidr))
print("Calculated mask = {}{}\n".format("255.255.255.", msk))
print("Subnet = {}{}\n".format(ipNetOcts, ipInt & msk))
print("Broadcast = {}{}\n".format(ipNetOcts, (ipInt & msk) + 2**(32 - cidr) - 1))

#-------------------------------------------------------------------------------------

cell = [(ix,iy) for ix, row in enumerate(vlsm) for iy, i in enumerate(row) if i == 50]

print("\n\n")
print(cell[0][0], " ", cell[0][1])
print("\n\n")

sn = vlsm[0:4]
# sn = im[4:8]
for r in sn:
    print(r[4:8])


print("\n\nsn = ", sn)

