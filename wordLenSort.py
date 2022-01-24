

'''
with open("en_US-large.txt", 'r') as wread:
    wr = wread.readlines()
    with open("wsort", 'w') as ww:
        for n in range(1, 47):
            for w in wr:
                if len(w) == n:
                    ww.write(w)
'''
'''
with open("wsort", 'r') as wread:
    wr = wread.readlines()
    with open("wsortlc", 'w') as ww:
        for w in wr:
            chc = ord(w[0])
            if(chc > 96 and chc < 123) and ("'" not in w):
                ww.write(w)
'''

with open("wsortlc", 'r') as wr:
    wlenDict = {}
    WL = wr.readlines()
    wlen = 0
    for i, w in enumerate(WL):
        if (len(w.strip()) > wlen):
            wlenDict[len(w.strip())] = i
            wlen = len(w.strip())

for i, k in enumerate(list(wlenDict.keys())):
    print('\t', k, wlenDict[k])

# [[s, e] for s, e in zip(list(wlenDict.keys())[0, -1], list(wlenDict.keys())[1, len(wlenDict.keys())-1])]

wlen = len(wlenDict.keys())
wk=[[s,e] for s, e in zip(list(wlenDict.keys())[0:-1], list(wlenDict.keys())[1:wlen])]
wk={k:[s,e] for k, s, e in zip(list(wlenDict.values()), list(wlenDict.keys())[0:-1],\
 list(wlenDict.keys())[1:wlen])}


[[wlenDict[K[0]], wlenDict[K[1]]] for K in wk]


