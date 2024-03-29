
import numpy as np
from os import system
cls = lambda: system("cls")

rv = [10.0, 11.0, 12.0, 13.0, 15.0, 16.0, 18.0, 20.0, 22.0, 24.0, 27.0, 30.0,
        33.0, 36.0, 39.0, 43.0, 47.0, 51.0, 56.0, 62.0, 68.0, 75.0, 82.0, 91.0]

V = 5
mv = {str(r)+' | '+str(s) : V * r / (r + s) for r in rv for s in rv}
# mvnp = np.array(list(mv.values()))

Vlist = [float(f"{n:.2f}") for n in mv.values()]


def vclose(Vin, Vout, tol):
    ''' list resistor pairs from rpair(Vs, Vo) results that
    output Volts with tolerance tol '''
    mv = {str(r)+' | '+str(s) : Vin * r / (r + s) for r in rv for s in rv}
    mvnp = np.array(list(mv.values()))
    VcloseInd = np.where(np.less(np.abs(mvnp - Vout), tol))
    Vclose = [list(mv.keys())[n] for n in list(VcloseInd[0])]
    dspVdiv(Vin, Vclose)
    return Vclose

def dspVdiv(Vin, RList):
    for R in RList:
        R0 = float(R.split()[0])
        R1 = float(R.split()[-1])
        print(f"\n\tVout = {Vin} * {R0} / ({R0} + {R1}) = {Vin * R0 / (R0 + R1):.3F}\n")
    print('\n')



def rpair(Vs, Vo):
    '''
    .
     Find the closest pair of common resistor values that will divide the
     voltage Vs to output Vo on a voltage divider wwhere
    .
     Vo = Vs * R[0] / (R[0] + R[1])
    .
    '''
    mv = {str(r)+' | '+str(s) : Vs * r / (r + s) for r in rv for s in rv}
    vals = np.array(list(mv.values()))
    minv = np.min(np.abs(vals - Vo))
    pm = np.any(np.where(vals == minv + Vo))
    if(pm):
        rp = np.where(vals == minv + Vo)[0][0]
    else:
        rp = np.where(vals == -minv + Vo)[0][0]
    RP = list(mv.keys())[rp]
    R0 = float(RP.split()[0])
    R1 = float(RP.split()[-1])
    print(F'\n\t5 * {R0} / ({R0} + {R1}) = {list(mv.values())[rp]:.3f}\n')
    return [R0, R1]


