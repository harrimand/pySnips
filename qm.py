#Quine McCluskey Aglorithm Module

#------------------------------------------------------------
def validDontCares(dontCare, data):
    """If item in dontCare list is found in data list
    item will be removed from dontCare list."""
    for d in dontCare:
        if d in data:
            dontCare.remove(d)
    return dontCare

#------------------------------------------------------------
def decList2binList(data):
    """Take a list of integers.  Return a list of
    binary strings padded with 0s to match the size of
    the binary representation of the largest integer in
    the list."""
    binData = []
    bitsize = max(data).bit_length()
    for b in data:
        setbits = bin(b)[2:].count("1")
        bitstr = ("{:0>{}}".format(bin(b)[2:], bitsize))
        binData.append(bitstr)
        #print("\t{}\t{}".format(bitstr, setbits))
    return binData

#------------------------------------------------------------
def mkSortByNumBitsSetDict(binData):
    """Take a list of binary strings and return a dictionary sorted by
    number of bits set in the strings.  Keys indicate number of bits set
    in each of the binary strings and values are lists of binary strings"""
    bDict = {}
    bitsize = len(binData[0])
    for i in range(bitsize + 1):
        bTemp = []
        for v in binData:
           if i == v.count("1"):
                bTemp.append(v)
        if len(bTemp):
            bDict[i] = bTemp
    return bDict

#------------------------------------------------------------
def mkEssDict(inDict):
    """Take input Dictionary and return matching
    sized dictionary with all values replaced with True"""
    tmpDict = {}
    for i in inDict:
        tmpDict[i] = ([True] * len(inDict[i]))
    return tmpDict

#------------------------------------------------------------
def compBin(astr, bstr):
    """Compare strings with matching lengths containing
    0s, 1s and Xs.
    If Xs are aligned in both strings and only one
    other character is different, return a string
    containing an X where a 1 in one string
    aligns with a 0 in the other string.
    If an appropriate comparison is not found,
    return an empty string."""
    result = ""
    chgCount = 0
    for c in range(len(astr)):
        if astr[c] == bstr[c]:
            result += astr[c]
        elif astr[c] != 'X' and bstr[c] != 'X':
            result += 'X'
            chgCount += 1
        else:
            result = ""
            break
    if chgCount > 1:
        result = ""
    return result

#------------------------------------------------------------
def copyPrimes(bDict, Essential, prime):
    """Copy strings in bDict identified as essential by
    True/False values in Essential and append to list
    prime"""
    for k in bDict:
        for i, v in enumerate(bDict[k]):
            if Essential[k][i]:
                prime.append(v)
#    print("\n\nPrimes: ",prime)
    return prime

#------------------------------------------------------------
def resetEssFlags(TempDict):
    """Take a dictionary with key:value pairs.
    keys are integers identifying number of bits set in all
    binary strings in lists
    values are lists of binary strings
    returns a dictionary with the same keys and all values
    containing boolean True"""
    bDictEssential = {}
    for k in TempDict:
        newlist = []
        for sz in range(len(TempDict[k])):
            newlist.append(True)
        bDictEssential[k] = newlist
    return bDictEssential

#------------------------------------------------------------
def decImps(term):
    """Parameter: String containing characters 1, 0 and X.
    Return list of all values where X's are replaced with all
    possible combinations of 1s and 0s"""
    numX = term.count("X")
    decList = []
    for b in range(2**numX):
        bbits = ("{:0>{}}".format(bin(b)[2:], numX))
        imp = term
        for bit in bbits:
            imp = imp.replace("X", bit, 1)
        decList.append(int(imp, 2))
    return(decList)

#------------------------------------------------------------
def binToVars(essStr):
    """Take a string containing 0s, 1s and Xs and return a string starting
    with A or !A if string starts with a 1 or 0 and exclude letters represented
    by X. Example:  X1X01 returns B !D E"""
    term = ""
    ch = 0
    for c in essStr:
        if c == '0':
           term += '!' + chr(ord('A') + ch) + ''
        elif c == '1':
            term += chr(ord('A') + ch) + ''
        ch += 1
    return term

#------------------------------------------------------------
def invList(imps):
    """Return a list of all integers less than or equal to the largest
    integer that can be represented with the bit size of the largest
    integer passed to the function and not included in the list passed
    to the function"""
    tmpList = []
    bitsize = max(imps).bit_length()
    for i in range(2**bitsize):
        if i not in imps:
            tmpList.append(i)
    return tmpList

#------------------------------------------------------------
def sortByCountX(prime):
    """Take a list of strings and return a list sorted by the
    number of Xs found in each string"""
    pTemp = []
    for i in range(len(prime[0]) + 1):
        for p in prime:
           if i == p.count("X"):
                pTemp.append(p)
    return pTemp

#------------------------------------------------------------
def v2bterms(instr, vars):
    """ parameters:
    string  "A!B!D" representing a product in a sum of products
    boolean expression.
    list ['A', 'B', 'C', 'D'] containing all variables in the sum
    of products expression.
    returns a string "10X0" with missing variables in string replaced
    with a "X".  """
    inlist = []
    c = 0
    while c < len(instr):
        if instr[c] == '!':
           inlist.append(instr[c] + instr[c+1])
           c += 2
        else:
            inlist.append(instr[c])
            c += 1
    #print("\n\n\tinstr: {}\n\n\tinlist: {}".format(instr, inlist))
    #print("\n\n\t vars: {}".format(vars))

    resb = ''
    for c in vars:
        if c not in inlist and ('!' + c) not in inlist:
            resb += 'X'
        elif c in inlist:
            resb += '1'
        else:
            resb += '0'
    #print("Result: {}".format(resb))
    return resb

#------------------------------------------------------------
def getVars(sop):
    '''Takes a string containing single character variables and makes a sorted
    list of the unique variables (Upper or Lower Case) found in the string.
    Non alpha characters will not be included in the list
    Ex: "AC!D + !AB!D+A!B" returns ['A', 'B', 'C', 'D']'''
    vars = []
    for c in sop:
        if (ord(c) > 64 and ord(c) < 91 or ord(c) > 97 and ord(c) < 123)\
        and c not in vars:
            vars.append(c)
    vars.sort()
    return vars

#------------------------------------------------------------
def sop2imps(sop, vars):
    '''Parameters: sop: String containing a SOP (sum of products)
                   vars: list containing variables
    vars may include variables not in sop string
    Returns sorted list of all implicants covered by the sop'''
    soplist = ' _ '.join(sop.split('+')).replace(' ', '').split('_')
#    print(sop, "\n\n ", soplist, "\n\n") #Comment

    covers = []
    for T in soplist:
        covers.append(v2bterms(T, vars))
#    print("\n\t", covers, "\n") #Comment

    coverImps = []
    for term in covers:
        for I in decImps(term):
            if I not in coverImps:
                coverImps.append(I)
    coverImps.sort()
    return coverImps

#------------------------------------------------------------
def impStr2impList(impStr, sort=1):
    '''Parameter:  A string containing decimal integers seperated by commas or
    spaces.  Range operators (..) are interpreted as follows:
    ..3 [0, 1, 2, 3]  #include all integers from 0 to 3
    6..10 [6, 7, 8, 9, 10]  all integers from 6 to 10 inclusive.
    5..  [5, 6, 7]  include all 3 bit integers starting at 5.  5 is a 3 bit int.
    12.. [12, 13, 14, 15]  include all 4 bit integers starting at 12.
    Return a sorted unique list of all integers in string including ranges.'''
    imptmp = impStr.replace(", ", " ")
    implist = ' '.join(imptmp.split()).split()
    decimps = []
    for i in implist:
        if ".." not in i:
            if i not in decimps:
               decimps.append(int(i))
        elif i.find("..")+2 == len(i):
            seqEnd = pow(2, int(i[:i.find("..")]).bit_length())
            for n in range(int(i[:i.find("..")]),seqEnd):
                if n not in decimps:
                    decimps.append(n)
        elif i.find("..") == 0:
            for n in range(0, int(i[i.find("..")+2:])+1):
               if n not in decimps:
                  decimps.append(n)
        else:
            for n in range(int(i[:i.find("..")]),int(i[i.find("..")+2:])+1):
               if n not in decimps:
                  decimps.append(n)
    if(sort):
        decimps.sort()
    return decimps

#------------------------------------------------------------
# def ___impStr2impList(impStr):
    '''Take a poorly formated string containing integers, spaces, commas,
    and range operators [".."] and return a list containing integers with
    range operators expanded to include all integers between operands.
    Range Operator 5..8 expands to [5, 6, 7, 8]
    Example:  impStr "0, 1   3, 5..9, 12    13 15"
        returns [0, 1, 3, 5, 6, 7, 8, 9, 12, 13, 15]'''
'''
    imptmp = impStr.replace(", ", " ")
    implist = ' '.join(imptmp.split()).split()
    decimps = []
    for i in implist:
        if ".." not in i:
            decimps.append(int(i))
        else:
            for n in range(int(i[:i.find("..")]),int(i[i.find("..")+2:])+1):
                decimps.append(n)
    return decimps
'''

#------------------------------------------------------------
def tt2ssop(data, dontCare):
    '''Parameters: data = list of all integers with true output
    on truth table.  dontCare = list of integers where output is
    of no concern.  dontCare outputs are not required to be included in table
    generated by simplified Sum of Products.
    Return boolean expression for simplified Sum of Products (SOP)'''

#    dontCare = validDontCares(dontCare, data)
    data.extend(dontCare)
    data.sort()
#    dontCare = validDontCares(dontCare, data)
    binData = decList2binList(data)
    bDict = mkSortByNumBitsSetDict(binData)
    bDictEssential = mkEssDict(bDict)
    prime = []
    done = False
    while not done:
        done = True
        TempDict = {}
        for b1 in bDict:

            newList = []
            if (b1+1) in bDict:
                for h, bt in enumerate(bDict[b1]):

                    for i, b2 in enumerate(bDict[b1+1]):

                        res = compBin(bt, b2)
                        if res != "":
                            done = False
                            bDictEssential[b1+1][i] = False
                            bDictEssential[b1][h] = False
                            newList.append(res)

            if newList != []:
               TempDict[b1] = list(set(newList))

        copyPrimes(bDict,bDictEssential, prime)
        bDictEssential = resetEssFlags(TempDict)
        bDict = TempDict

    prime = list(set(prime))
    prime.sort()
    prime = sortByCountX(prime)
    essentialFlag = []
    impList = []
    impFlat = []

    for p in prime:
        imp = decImps(p)
        impList.append(imp)
        essentialFlag.append(False)
        for v in imp:
            impFlat.append(v)

    impFlat.sort()

    for i, p in enumerate(impList):
        ess = False
        for c in p:
            if impFlat.count(c) == 1 and c not in dontCare:
                ess = True
                essentialFlag[i] = True
        if not ess:
            for c in p:
                impFlat.remove(c)
            essentialFlag[i] = False

    essTerms = []
    for i, p in enumerate(prime):
        if essentialFlag[i]:
            essTerms.append(p)

    essList = []
    for t in essTerms:
        essList.append(binToVars(t))

    essList.sort()

    SOPstring = ""
    for i, t in enumerate(essList):
        SOPstring += t
        if i < (len(essList) - 1):
            SOPstring += " + "
    return SOPstring
#------------------------------------------------------------
'''
    for i, p in enumerate(impList):
        ess = False
        for c in p:
            if impFlat.count(c) == 1 and c not in dontCare:
                ess = True
                essentialFlag[i] = True
        if not ess:
            for c in p:
                impFlat.remove(c)
            essentialFlag[i] = False

    essTerms = []
    for i, p in enumerate(prime):
        if essentialFlag[i]:
            essTerms.append(p)

    essList = []
    for t in essTerms:
        essList.append(binToVars(t))

    SOPstring = ""
    for i, t in enumerate(essList):
        SOPstring += t
        if i < (len(essList) - 1):
            SOPstring += " + "
    return SOPstring
'''

#------------------------------------------------------------
def tt2usop(data):
    '''Parameter: List containing integers that produce True
    on the output of the Sum of Products (SOP).
    Returns an Unsimplified SOP that covers all integers in List.'''
    termList = []
    bitsize = max(data).bit_length()
    for d in data:
        termList.append(binToVars(bin(d)[2:].zfill(bitsize)))
    SOPstring = ""
    for i, t in enumerate(termList):
        SOPstring += t
        if i < (len(termList) - 1):
            SOPstring += " + "
    return SOPstring

#------------------------------------------------------------
def subVars(SOP, oldVars, newVars):
    '''Parameters: SOP = string containing Sum Of Products
    oldVars: String containing characters to be replaced.
    newVars: String containing characters that will replace characters in oldVars
    Will search SOP for characters in oldVars and replace them with corresponding
    characters in newVars.  Replacement will stop at the end of the shortest string.
    Returns SOP with characters replaced.'''
    for i in range(min(len(oldVars), len(newVars))):
        SOP = SOP.replace(oldVars[i], newVars[i])
    return SOP

#------------------------------------------------------------
def sop2htm(sop):
    '''Takes a string containing a Sum of Products and inserts html tags for
    every '!' to overline the following variable.
    Returns a string containing html tags to make the SOP pretty in a browser.'''
    htmb = "<span style=\"text-decoration: overline\"><b>"
    htma = "</b></span><nbsp>"
    notVar = False
    htmstr = ""

    for c in sop:
        htmstr += " "
        if c == '!':
            notVar = not notVar
        elif notVar:
            htmstr += htmb + c + htma
            notVar = not notVar
        else:
            htmstr += "<b>" + c + "</b>"
    return(htmstr)

#------------------------------------------------------------
def subSop2qm(mySop):
    '''Parameter mySop = string containing upper
    and lower case characters including the '!' and
    '+' operators and spaces. A sorted set of
    characters in the string are mapped to
    upper case alpha characters A..Z for processing
    with the Quine McCluskey algorithm.
    Returns a string with all alpha characters
    replaced with A..Z'''
    newSop = mySop
    mySopVars = []
    for c in mySop:
        if ord(c) >= 64 and ord(c) <= 90\
        or (ord(c) >= 97 and ord(c) <= 122):
            if c not in mySopVars:
                mySopVars.append(c)
    mySopVars.sort()
    ch = 65
    sopMap = {}
    for c in mySopVars:
        sopMap[chr(ch)] = c
        ch += 1
    for c, in sopMap.keys():
        newSop = newSop.replace(sopMap[c], c)
    return newSop

#------------------------------------------------------------
def subQm2sop(qmSop, mySop):
    '''Parameter qmSop is a modified string containing
    characters A..Z + '+' + '!'.
    Parameter mySop = string containing upper
    and lower case characters including the '!' and
    '+' operators and spaces. A sorted set of
    characters in the string are mapped to
    upper case alpha characters A..Z that were used
    to process the Quine McCluskey algorithm.
    Returns a string with characters A..Z replaced
    with mapped characters from the mySop string.'''
    mySopVars = []
    for c in mySop:
        if ord(c) >= 64 and ord(c) <= 90\
        or (ord(c) >= 97 and ord(c) <= 122):
            if c not in mySopVars:
                mySopVars.append(c)
    mySopVars.sort()
    ch = 65
    sopMap = {}
    for c in mySopVars:
        sopMap[chr(ch)] = c
        ch += 1
    for c, in sopMap.keys():
        qmSop = qmSop.replace(c, sopMap[c])
    return qmSop

#------------------------------------------------------------
def qmSimp(thing, DontCare=[], includeVars=""):
    '''Parameters:
        thing:  List of integers (implicants) that produce a true
        output on the boolean expression. Eg: [1, 4, 8, 12, 24]
                String containing integers (implicants) that produce
        a true output on the boolean expression.  String may contain
        range operators.  Eg: "..3, 5..,10, 13..17 25, 29.."
        is a valid list that will be converted to
        [0, 1, 2, 3, 5, 6, 7, 10, 13, 14, 15, 16, 17, 25, 29, 30, 31]
        ..3 produces all integers from 0 to 3.
        5.. produces all 3 bit numbers >= 5. (5 is a 3 bit number)
        13..17 produces 13, 14, 15, 16, 17
        29.. produces all 5 bit numbers >= 29
        Seperators may be spaces or commas.
                String containing a Sum of Products (SOP) expression.
        Eg:  "!CAD+ A!B D +  !DA!C + !DB " is a valid expression.
        ! is a NOT operator.  + is an OR operator.  All variables not
        seperated by an OR operator are ANDed together. All variables
        are represented by a single character A,B,C...

        [DontCare]: Optional list or string containing integers meeting
        the same criteria as the 'thing' parameter.

        [includeVars]: Optional string containing aditional variables
        that may not be in the Sum of Products string. Eg: "D EF" will
        add 3 bits to the truth table inputs.

        Returns a simplified Sum of Products.'''
    #print("\n\nThing: ", thing, type(thing))
    #print("Don't Care: ", DontCare, type(DontCare))
    #Checking DontCare
    if isinstance(DontCare, list):
        isIntList = True
        for i in DontCare:
            if not isinstance(i, int):
                isIntList = False
        if not isIntList:
            print("Don't Care List Invalid")
            return
        else:
            DC = DontCare
    elif isinstance(DontCare, str):
        isIntStr = True
        for i in DontCare:
            if not (i.isdigit() or i.isspace() or i == ',' or i == '.'):
                isIntStr = False
        if isIntStr:
            DC = impStr2impList(DontCare)
        else:
            print("Don't Care String Invalid")
            return
    else:
        print("ERROR! Don't Care List must be a String or List")
        return
    #Checking thing
    if isinstance(thing, str):
        isSOP = True
        isIntStr = True
        for c in thing: #Verify Valid Sum of Products or Integer String
            if not (c.isalpha() or c.isspace() or c == '+' or c == '!'):
                isSOP = False
            if not (c.isdigit() or c.isspace() or c == ',' or c == '.'):
                isIntStr = False
        if isSOP:
            tt = sop2imps(thing, getVars(thing + includeVars))
            return tt2ssop(tt, DC)
        elif isIntStr:
            tt = impStr2impList(thing)
            return tt2ssop(tt, DC)
        else:
            print("!!!_INVALID String_!!!")
    elif isinstance(thing, list):
        isIntList = True
        for i in thing: #Verify List contains only integers
            if not isinstance(i, int):
                isIntList = False
        if isIntList:
            return tt2ssop(thing, DC)
        else:
            print("!!!_INVALID Integer List_!!!")
    else:
        print("Thing is not a String or a List")

#------------------------------------------------------------

def qmHelp():
    print('\tgetVars(sop):')
    print('\tsop2imps(sop, vars):')
    print('\timpStr2impList(impStr):')
    print('\ttt2ssop(data, dontCare):')
    print('\ttt2usop(data):')
    print('\tsubVars(SOP, oldVars, newVars):')
    print('\tsop2htm(sop):')
    print('\tsubSop2qm(mySop):')
    print('\tsubQm2sop(qmSop, mySop):')
    print('\tqmSimp(thing, DontCare=[], includeVars=""):')

    print('_'*80, '\n\n\t\tExample Usage:\n')

    print(" from qm import *")
    print(" impStr = '1.. 5 7..9, 11'")
    print(" dcStr = '12..'")
    print(" tt = impStr2impList(impStr)")
    print(" tt")
    print(" [1, 5, 7, 8, 9, 11]")
    print(" dc = impStr2impList(dcStr)")
    print(" dc")
    print(" [12, 13, 14, 15]")
    print(" usop = tt2usop(tt)")
    print(" usop")
    print(" '!A!B!CD + !AB!CD + !ABCD + A!B!C!D + A!B!CD + A!BCD'")
    print(" ssop = tt2ssop(tt, dc)")
    print(" ssop")
    print(" '!CD + A!C + AD + BD'")
    print(" Vars = getVars(usop)")
    print(" Vars")
    print(" ['A', 'B', 'C', 'D']")
    print(" terms = ssop.split(' + ')")
    print(" terms")
    print(" ['!CD', 'A!C', 'AD', 'BD']")
    print(" for t in terms:")
    print("     print('\\n\\t', t.ljust(8, '_'), sop2imps(t, Vars))")

    print("\n\t", "!CD".ljust(8, "_"), "[1, 5, 9, 13]")
    print("\n\t", "A!C".ljust(8, "_"), "[8, 9, 12, 13]")
    print("\n\t", "AD".ljust(8, "_"), "[9, 11, 13, 15]")
    print("\n\t", "BD".ljust(8, "_"), "[5, 7, 13, 15]")
    print('\n\n', '_'*80, '\n\n')

#------------------------------------------------------------


