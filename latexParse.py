# Boolean Logic conversion to LaTex format
# Author:  Darrell Harriman
# harrimand@gmail.com

def latexParse(boolExp):
    """ LatexParse(boolExp) parses boolean expression to LaTex
    eg: latexParse("!(!(Abc) !(!A B !C)) + !(A ^ B)")
    '!' are replaced with \overline or \bar
    '(' and ')' replaced with '{' and '}'
    '^' for XOR is replaced with \oplus"""

    boolExp =  boolExp.replace('(', '{')
    boolExp =  boolExp.replace(')', '}\;')

    while '!' in boolExp:
        i = boolExp.find('!')
        if boolExp[i+1:].strip()[0] == '{':
            boolExp = boolExp.replace('!', "\;\overline",1)
        else:
            boolExp = boolExp.replace('!', "\\bar ", 1)

    boolExp = boolExp.replace('^', "\;\oplus\;")
    boolExp = boolExp.replace(" \\", "\\")
    boolExp = boolExp.replace("\; ", "\;")

    return "$" + boolExp + "$"


bExp = "!(!(Abc) !(!A B !C)) + !(A ^ B)"
print("\nbExp: ", bExp)

testExp = "$\;\overline{\;\overline{Abc}\;\;\overline{\\bar A\;B\;\\bar C}\;}\;+\;\;\overline{A\;\oplus\;B}\;$"
print('\n\n', testExp)

Latex =  latexParse(bExp)
print('\n', Latex)

S = "C ^ A ^ B"
# C = (A B) ^ (C (A ^ B))
# C = (A B) ^ (C (A!B + !AB))
# C = (A B) ^ (CA!B + C!AB)
# C = (A B) !(CA!B + C!AB) + !(A B) (CA!B + C!AB)
# C = (A B) !(CA!B + C!AB) + !(A B) C A !B + !(A B) C !A B
C = "A B !(CA!B + C!AB) + !(A B) C A !B + !(A B) C !A B"


# C = "A B !(C !A B + C A !B) + !(A B) C !A B + C A !B"

print("\nFull Adder:\nSum = ", latexParse(S))
print("\nCary = ", latexParse(C))


""" OUTPUT
bExp:  !(!(Abc) !(!A B !C)) + !(A ^ B)

$\;\overline{\;\overline{Abc}\;\;\overline{\bar A\;B\;\bar C}\;}\;+\;\;\overline{A\;\oplus\;B}\;$

$\;\overline{\;\overline{Abc}\;\;\overline{\bar A B\bar C}\;}\;+\;\overline{A\;\oplus\;B}\;$

"""
