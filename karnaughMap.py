

tts = "1..3 5.. 9..11 13, 14"
# tt = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14]

tt = [6, 7, 8, 10, 12, 14, 15]

#-------------------------------------------------------------------

gc = [n ^ n>>1 for n in range(16)]

KMapL = lambda imps: [['1' if gc[o] in imps else '0'\
        for o in range(*[[n,n+4,1],[n+3,n-1,-1]][(n//4)%2])] for n in range(0,len(gc),4)]

#-------------------------------------------------------------------
#
def karnaughMap(imps, padL):
    """Generate list of strings formatted for printing Karnaugh Map
    KMap = 2D List of 1s and 0s to be filled in on karnaugh Map
    padl = padding on left side for table output
    return list of even length strings to print Karnaugh Map i"""
    KMap = KMapL(imps)

    kMapList = []
    kMapList.append(' ' * padL + ' '*18 + '-'*8 + '          |')
    kMapList.append(' ' * padL + ' '*17 + '|' + '        ' +  '|         |')
    kMapList.append(' ' * padL + ' '*17 + '|' + '    C   ' +  '|         |')
    kMapList.append(' ' * padL + ' '*17 + '|' + '        ' +  '|         |')
    kMapList.append(' ' * padL +  ' '*7 + '-'*20+'         |')
    kMapList.append(' ' * padL +  ' '*6 + '|' + ' '*20 + '|        |')

    kMapStr = ' ' * padL +  ' '*6 + '|'
    row = 0
    for c in range(row * 4, row * 4 + 4):
        kMapStr += f"  { KMap[row][c] }  "
    kMapStr += '|        |'
    kMapList.append(kMapStr)

    kMapStr = ' ' * padL + ' '*6 + '|' + ' '*19 + ' |-----   |'
    kMapList.append(kMapStr)

    kMapStr = ' ' * padL + ' ' * 6 + '|'
    row += 1
    for c in range(4):
        kMapStr += f"  {  KMap[row][c] }  "
    kMapStr += '|     |  |'
    kMapList.append(kMapStr)

    kMapStr = ' ' * padL + ' '*1 + '-----' + '|' + ' '*19 + ' |  B  |  |'
    kMapList.append(kMapStr)

    kMapStr = ' '* padL + '|     |'
    row += 1
    for c in range(4):
        kMapStr += f"  {  KMap[row][c] }  "
    kMapStr += '|     |  |'
    kMapList.append(kMapStr)

    kMapStr = ' ' * padL + '|  A  |' + ' '*19 + ' |-----   |'
    kMapList.append(kMapStr)

    kMapStr =  ' ' * padL + '|     |'
    row += 1
    for c in range(4):
        kMapStr += f"  {  KMap[row][c] }  "
    kMapStr += '|        |'
    kMapList.append(kMapStr)

    kMapStr = ' ' * padL + ' '*1 + '-----' + '|' + ' '*19 + ' |        |'
    kMapList.append(kMapStr)

    kMapList.append(' ' * padL + ' '*7 + '-'*20+'         |')
    kMapList.append(' ' * padL + ' '*12 + '|' + '         ' +  '|             |')
    kMapList.append(' ' * padL + ' '*12 + '|' + '    D    ' +  '|             |')
    kMapList.append(' ' * padL + ' '*12 + '|' + '         ' +  '|             |')
    kMapList.append(' ' * padL + ' '*13 + '-'*9 + '              |')
    return kMapList

kMapStr = karnaughMap(tt, 10)

for k in kMapStr:
    print(k)

with open('kmTxt', 'w') as kmfile:
    kmfile.write("\n\n")
    kmfile.write("Implicants: ")
    kmfile.write(" ".join([str(Imp) for Imp in tt]))
    kmfile.write("\n\n")
    for k in kMapStr:
        kmfile.write(k+"\n")






