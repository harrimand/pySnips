

from word_en import *
from random import randint


# XX = "abcde"

lsub = lambda s, L, p: "".join([S if i != p else L for i, S in enumerate(s)])
lsubUp = lambda s, L, p: "".join([S.upper() if i != p else L.upper() for i, S in enumerate(s)])

def wordle():
    x = words("_____")
    XX = x.words[randint(0, len(x.words))]
    while((G := input("\tGuess a word: ")) != 'q'):
        X = XX
    #    print("G = ", G, " X = ", X)
        res = "_____"
        for i, l in enumerate(G):
            if l == X[i]:
                res = lsubUp(res, l, i)
                G = lsub(G, '_', i)
                X = lsub(X, '_', i)
    #    print(F"Correct letter positions: {res}")
    #    print(F"Remaining Guess Letters: {G}")
        for i, l in enumerate(G):
            if l != '_':
    #            print(F"Checking {l} at pos {i}", end=' ')
                j = 0
                while(res[j] != '_'):
                    j += 1
                if l in X:
                    res = lsub(res, l, i)
                    X = X.replace(l, '_')
    #                print(F"New res: {res} X = {X}")
                else:
                    pass
        print(F"\t      Result: {res}")






