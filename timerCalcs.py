

from math import log10, floor
import numpy as np
import pandas as pd

fixe = lambda n: log10(n)//3 * 3
feng = lambda n: F"{n / 10** fixe(n)} E {int(fixe(n))}".replace(" ","")
fng = lambda n: eval(feng(n))

def engn(n):
    e = log10(n)//3 * 3
    en = F"{n / 10** e} E {floor(e)}"
    return eval(en.replace(" ",""))

MCUclk = 1E6
clkPre = 64
T_t1 = clkPre / MCUclk

t = feng(T_t1)
print(t)
print(feng(T_t1))


CS1n = {0:"000", 1:"001", 8:"010", 64:"011", 256:"100", 1024:"101"}
mcuClk = [1, 4, 8, 16, 20]
t1data = [[cs / (t*1E6) * 2**16 for cs in CS1n.keys()] for t in mcuClk]

t1df = pd.DataFrame(t1data, index=mcuClk, columns=CS1n.values())
print(t1df)

tmax = np.array([[feng(n) for n in cpuclk if n > 0] for cpuclk in t1data])
trim = lambda ft, n: ft[:ft.index(".")+n+1]+ft[ft.index("E"):]
tm = [[trim(n, 2) for n in clk] for clk in tmax]
tmdf = pd.DataFrame(tm, index=mcuClk, columns=list(CS1n.values())[1:])
print('\n')
print("Max timer overflow time at common frequencies per clock select values")
print(tmdf)


with open("mcucs.html",  "w") as mc:
    mc.write("<html>\n")
    mc.write("<head>\n")
    mc.write("\t<style>\n")
    mc.write("\t\ttd{padding: 15px;}\n")
    mc.write("\t</style>\n")
    mc.write("</head>\n")
    mc.write("<body>\n")
    mc.write(tmdf.to_html(border=0, justify='center'))
    mc.write("\n</body>\n")
    mc.write("</html>\n")

