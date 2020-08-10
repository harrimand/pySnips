

# sop = "!AB!CD + A!B!C!D + A!BCD + AB!CD"
# sop = "!A!B!C!D + !A!BCD + !ABCD + A!B!CD + A!BCD + AB!CD + ABCD"
# sop = "!AB + A!B"
# sop = "!A!BC + !AB!C + Ai!B!C + ABC"
# sop = '!A!BC + !AB!C + !ABC + A!BC + AB!C + ABC'

# sop = '!A!BC!D + !A!BCD + !ABC!D + !ABCD + A!B!C!D + A!B!CD + AB!C!D + AB!CD'

sop = '!A!B!C!D + !A!B!CD + !A!BC!D + !A!BCD + !AB!C!D + !ABC!D + A!B!C!D + A!B!CD'

sop = sop.replace(' ', '')
next = False
lstr = ''
for i, ch in enumerate(sop):
    if next:
        next = False
        continue
    elif ch == '!':
        lstr += '\overline{' + sop[i+1] + '}\;'
        next = True
    else:
        lstr += ch + '\;'

lstr = lstr[:-2]

print('\n\n', sop, '\n\n')
print('\n\n', lstr, '\n\n')


