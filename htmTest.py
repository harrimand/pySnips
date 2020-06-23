
import qm

# tt = "..3 5.., 10, 13..17 25, 29.."
# tt = "3 6..8 11, 12, 15"
# tt = "2, 4, 6..9, 13.."
# tt = "1..3 5.. 9..11 13, 14"
tt = " ".join([str(n) for n in range(2**4) if (bin(n)[2:].count('1')%2 == 1)])
print("\n\n\ttt: ", tt, "\n\n")


dc = []
fileName = 'boolExp5.htm'
pageTitle = 'Boolean Expression'


imps = qm.impStr2impList(tt)
ssop = qm.qmSimp(tt, dc)
usop = qm.tt2usop(imps)
bitLen = max(imps).bit_length()
maxImp = 2**bitLen - 1
qvars = [chr(c) for c in range(65, 65 + bitLen)]
# usopHtm = '<p>' + qm.sop2htm(usop) + '</p>'
# ssopHtm = '<p>' + qm.sop2htm(ssop) + '</p>'
usopHtm = qm.sop2htm(usop)
ssopHtm = qm.sop2htm(ssop)


head = '\n\n<header>\n<h1>Boolean Expression</h1>\n</header>'

boolExp = '\n\n<div class="boolExp">\n' + usopHtm + '\n</div>\n'
# boolExp = '\n\n<div id="boolExp">\n' + usopHtm + '\n</div>\n'

padLeft = '\n\n<div class="padLeft">\n' + "<p>..</p>" + '\n</div>\n'


#-------------------------------------------------------------------

terms = ssopHtm.split('+')
cterms = ssop.split(' + ')
covers = []
print("\n\nImplicants: ", imps, '\n')
for term, cterm in zip(terms, cterms):
    cov = qm.decImps(qm.v2bterms(cterm, qvars))
    covers.append(cov)
    print(cterm.rjust(9), cov)
print('\n\n')

tcov = '<table id="t02">\n'
tcov += '<tr>\n'
tcov += '\t<th>TERM</th>\n'
for i in imps:
    tcov += '\t<th>' + str(i) + '</th>\n'
tcov += '</tr>\n'
for t, term in enumerate(terms):
    tcov += '<tr>'
    tcov += '<td>' + term + '</td>'
    for i in imps:
        if i in covers[t]:
            tcov += '<td><b>X</b></td>'
        else:
            tcov += '<td><b>&nbsp;</b></td>'
    tcov += '</tr>\n'
tcov += '\n</table>\n'

#-------------------------------------------------------------------
tstr = '<table id="t01">\n'
tstr += '<tr>\n'
tstr += '\t<th>Dec</th>\n'
for q in qvars:
    tstr += '\t<th>'+q+'</th>\n'
tstr += '\t<th>'+'Q'+'</th>\n'
tstr += '</tr>\n'
for i in range(maxImp+1):
    tstr += '<tr>'
    tstr += '<td>'+str(i)+'</td>'
    for b in bin(i)[2:].zfill(bitLen):
        tstr += '<td>'+str(b)+'</td>'
    if i in imps:
        tstr += '<td>'+'<b>1</b>'+'</td>'
    else:
        tstr += '<td>'+'<b>0</b>'+'</td>'
    tstr += '</tr>\n'
tstr += '\n</table>\n'
#-------------------------------------------------------------------

truthTable = '\n\n<div class="truthTable">\n' + tstr + '\n</div>\n'


tbStr = '\n\ntable {\nwidth:25%;\nborder-collapse: collapse;\n}'
tbStr += '\n\nth, td {\npadding: 10px;\ntext-align: center;\n}'
tbStr += '\n\n #t01 th, td {\nborder: 2px solid black;\nborder-collapse: collapse;\n}'
tbStr += '\n\n #t01 tr:nth-child(even) {\nbackground-color: #eee;\n}'
tbStr += '\n\n #t01 tr:nth-child(odd) {\nbackground-color: #fff;\n}'
tbStr += '\n\n #t01 th {\nbackground-color: black;\ncolor: white;\n}'


tbStr2 = '\n\ntable {\nwidth:50%;\nborder-collapse: collapse;\n}'
tbStr2 += '\n\nth, td {\npadding: 10px;\ntext-align: center;\n}'
tbStr2 += '\n\n #t02 th, td {\nborder: 2px solid black;\nborder-collapse: collapse;\n}'
tbStr2 += '\n\n #t02 tr:nth-child(even) {\nbackground-color: #eee;\n}'
tbStr2 += '\n\n #t02 tr:nth-child(odd) {\nbackground-color: #fff;\n}'
tbStr2 += '\n\n #t02 th {\nbackground-color: black;\ncolor: white;\n}\n'


htmStr = '<!DOCTYPE html>\n\
<html>\n\
<head>\n\
<meta name="viewport" content="width=device-width, initial-scale=1">\n\
<style>\n\
* {\n\
  box-sizing: border-box;\n\
}\n\
.head2 {\n\
background: #abc;\n\
}\n\
\n\
/* Create two equal columns that floats next to each other */\n\
.columnL {\n\
  float: left;\n\
  width: 50%;\n\
  padding: 50px;\n\
}\n\
.columnR {\n\
  float: left;\n\
  width: 50%;\n\
  padding: 50px;\n\
}\n\
/* Clear floats after the columns */\n\
.row:after {\n\
  content: "";\n\
  display: table;\n\
  clear: both;\n\
}\n\
footer {\n\
}\n'
htmStr += tbStr
htmStr += tbStr2
htmStr += '</style>\n\
</head>\n\
<body>\n\
\n\
<h2>Boolean Expression | Truth Table | Simplified Boolean Expression</h2>\n'

htmStr += '<div class="head2">\n\
<p style="font-size:160%;" align="center"><br><b>' + usopHtm + '</b><br><br></p></div>\n\
<div class="row">\n\
  <div class="columnL" style="background-color:#fff;">\n\
    <h2>Term Coverages</h2>  \n'
htmStr += tcov
htmStr += ' </div>\n\
  <div class="columnR" style="background-color:#fff;">\n\
    <h3>Truth Table</h3>\n'

htmStr += tstr + '\n'

htmStr += '</div>\n\
</div>\n\
<footer style="background-color:#abc;">\n\
<p style="font-size:160%;" align="center"><br><b>' + ssopHtm + '</b><br>&nbsp;</p></footer>\n\
\n\
</body>\n\
</html>\n'

# print(htmStr)
print('\n file:///home/darrell/Documents/Python/QM_g/' + fileName + '\n')

with open(fileName, 'w') as f:
    f.write(htmStr)


# ToDo:  Debug  !ABC should be implicants 6 and 7.  getting 14, 15
#               A!C!D should be 8 and 12.  getting 11 and 15


