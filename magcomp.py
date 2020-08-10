
from qm import *

gt1 = "A!E"
gt2 = "B!F!A!E + B!FAE"
gt3 = "C!G!B!F!A!E + C!G!B!FAE + C!GBF!A!E + C!GBFAE"
gt41 = "D!H!C!G!B!F!A!E + D!H!C!G!B!FAE + D!H!C!GBF!A!E + D!H!C!GBFAE"
gt42 = "D!HCG!B!F!A!E + D!HCG!B!FAE + D!HCGBF!A!E + D!HCGBFAE"
gt4 = gt41 + " + " + gt42

gt = gt1 + " + " + gt1 +  " + " + gt3 +  " + " + gt4


eq1 = "!A!E!B!F!C!G!D!H + !A!E!B!F!C!GDH + !A!E!B!FCG!D!H + !A!E!B!FCGDH + !A!EBF!C!G!D!H + !A!EBF!C!GDH + !A!EBFCG!D!H + !A!EBFCGDH"
eq2 = "AE!B!F!C!G!D!H + AE!B!F!C!GDH + AE!B!FCG!D!H + AE!B!FCGDH + AEBF!C!G!D!H + AEBF!C!GDH + AEBFCG!D!H + AEBFCGDH"
eq = eq1 +  " + " + eq2


lt1 = "!AE"
lt2 = "!BFAE + !BF!A!E"
lt3 = "!CG!B!F!A!E + !CG!B!FAE + !CGBF!A!E + !CGBFAE"
lt41 = "!DH!C!G!B!F!A!E + !DH!C!G!B!FAE + !DH!C!GBF!A!E + !DH!C!GBFAE"
lt42 = "!DHCG!B!F!A!E + !DHCG!B!FAE + !DHCGBF!A!E + !DHCGBFAE"
lt4 = lt41 + " + " + lt42

lt = lt1 +  " + " + lt2 +  " + " + lt3 +  " + " + lt4

def logisim(sop):
    """ Insert spaces between variables for Logisim compatibility"""
    return " ".join(list(sop)).replace('! ', '!').replace('  +  ', ' + ')

GT = logisim(gt)
EQ = logisim(eq)
LT = logisim(lt)

print('\n\n', GT)
print('\n\n', EQ)
print('\n\n', LT)



