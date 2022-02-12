
import serial
import time

ser = serial.Serial(port='COM17', baudrate=115200)

lastS = .5
oldts = time.perf_counter()

while(1):
    if(ser.inWaiting() > 0):
        ts = time.perf_counter()
        dts = ts - oldts
        S = int(ser.readline().decode().rstrip())
        ud = " + " if S > lastS else " - "
        lastS = S
        print(S, ud, dts)
        oldts = ts



