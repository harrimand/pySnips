
from os import system
cls = lambda: system("clear")

'''
Dictionwary File download available at:
https://sourceforge.net/projects/wordlist/files/speller/2020.12.07/wordlist-en_US-large-2020.12.07.zip/download
'''


class words():
    def __init__(self, st, cc=0, letterReject=''):
        self.st = st
        self.letterReject = letterReject
        self.wind = self.wordIndex()
#        self.filePath = self.FPpath(st, cc)
#        self.words = self.WLinit(self.filePath)
        self.words = self.WLinit(cc)
        self.longest = self.wind[list(self.wind.keys())[-1]][1]
#        self.words = self.listFind(cc)
        self.listFind(self.st, letterReject)
        self.wlast = self.words

    '''
    def FPpath(self, st, cc):
        if cc > 2 and cc < 10:
            FP = './words' + str(cc)
        elif len(st) > 2 and len(st) < 10:
            FP = './words' + str(len(st))
        else:
            print("Invalid length. Must be 3..9")
            return
        return FP
    '''

    def wordIndex(self):
        ws =  open("wsortlc", 'r')
        WL = ws.readlines()
        ws.close()

        ind = 0
        indDict = {1:[0]}
        wlen = 1
        for i, w in enumerate(WL):
            nlen = len(w.strip())
            if(nlen > wlen):
                indDict[wlen].append(i)
                indDict[nlen] = [i]
                wlen = nlen
        indDict[nlen].append(i)
        # print(WL[:5])
        # print(WL[-5:])
        # print(len(w))
        # print("\tInd45: ", WL[indDict[45][1]])
        return indDict
    '''
    def wordsLen(self, cc):
        n = cc if cc > 0 else len(self.st)
        if (n in list(self.wind.keys())):
            return self.WL[self.wind[n][0]:self.wind[n][1]]
        else:
            return ["-"]
    '''

    def WLinit(self, cc):
        ws =  open("wsortlc", 'r')
        WL = ws.readlines()
        ws.close()
        n = cc if cc > 0 else len(self.st)
        if (n in list(self.wind.keys())):
            return WL[self.wind[n][0]:self.wind[n][1]]
        else:
            return ["-"]

    def listFind(self, st, letterReject=''):
        self.wlast = self.words
        uc = [c.lower() if (ord(c) > 64 and ord(c) < 92) else '_' for c in st]
        lc = [l for l in st if ord(l) > 96 and ord(l) < 124]
        if len(letterReject) > 0:
            self.letterReject += letterReject
            self.elim(letterReject)
        words = []
        for w in self.words:
            match = True
            for i, u in enumerate(uc):
                # print('\t', i, u, w[i], end=' ')
                if((u != '_') and (u != w[i])):
                    # print("F", end='')
                    match = False
                else:
                    pass
            if(match):
                for c in lc:
                    if c not in w:
                        match = False
                    if (lc.count(c) + uc.count(c)) > w.count(c):
                        match = False
            if(match):
                words.append(w.strip())
        print("\n\tWords Found: ", len(words), '\n')
        self.words = words

    def elim(self, ni):
        '''Remove all words containing letters in ni from list WW'''
        self.wlast = self.words
        uc = [c.lower() if (ord(c) > 64 and ord(c) < 92) else '_' for c in ni]
        lc = [l for l in ni if ord(l) > 96 and ord(l) < 124]
        self.letterReject += ni
        NL = []
        for w in self.words:
            F = True
            for L in w:
                if L in lc:
                    F = False
            for i, L in enumerate(uc):
                if L == w[i]:
                    F = False
            if F:
                NL.append(w)
        print(F"Remaining words: {len(NL)}\n")
        self.words = NL

    def sh(self, cols=4):
        cw = len(self.words[0])
        print('\n\t', end='')
        for i, w in enumerate(self.words):
            print(w.ljust(cw+3), end='')
            print('\n\t' if ((i+1) % cols) == 0 else '', end='')
        print("\n\n")

    def undo(self):
        self.words = self.wlast
        print(F"Remaining words: {len(self.words)}\n")

    def help(self):
        helpStr = '\n\twords("_a_De_", 7, "rs") %Find 7 letter words containing\n\
        a and e with D as 4th and not containing r or s.\n\
        Word find utility that finds all words of specified length\n\
        in spell check file containing all lower case letters in any\n\
        position and words with letters matching postions of upper case\n\
        letters.  Optional integer specifying length.  If length  omitted,\n\
        the word length will match length of string.\n\
        \n\
        listFind(st, letterReject) Search current word list for words containing \n\
        all lower case letters in st and letters matching positions of \n\
        upper case letters in strings.  Optional letterReject string containing \n\
        letters.  All words containing letters in Letlim will be removed \n\
        from list.\n\
        \n\
        elim(ni) Remove words from list containing letters in string ni.\n\
        \n\
        sh(cols=4) show (print) word list with optional number of columns.\n\
        \n\
        undo() Undo last change by recovering archived word list\n'
        print(helpStr)

    def hlp(self):
        hlpStr = '\n\tw = words("_Sab_", [len], ["ex"])\n\
                    find words from file of optional length [len] including "s"\n\
                    as second letter with "a" and "b" anywhere and optional\n\
                    ["ex"] exdluding words containing "e" and "x". If [len]\n\
                    is not given, length of string "_Sab_" will be used.\n\
                w.listFind("cd") # Find words with "c" and "d" in current list\n\
                w.listFind("cd", "ef") # Find words with "c" and "d"\n\
                        exdluding "e" and "f" in current list\n\
                w.elim("_Mgh") find words excluding "M" as the second letter and
                "g" and "h" in any postiion in current list\n\
                w.sh(n=4) Show words in current list witn n columns.  default=4\n\
                w.undo() undo last change and restore last list.'
        print(hlpStr, '\n')






def wordQlen(st):
    G = []


