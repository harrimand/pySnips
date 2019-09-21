#! /usr/bin/env python3
# Author: Darrell harriman  harrimand@gmail.com
# Capture the current day's sun position data from the U.S. Naval Observatory website
# for a specified location and at a specified interval in minutes.
# Data is written to file sunTrack.txt and displayed on the console.

import urllib.request
import datetime

YY = datetime.date.today().strftime("%Y")
MM = datetime.date.today().strftime("%m")
DD = datetime.date.today().strftime("%d")

State = 'CA'
City = 'Victorville'
Interval = 10

# URL and Data assembled from  https://aa.usno.navy.mil/data/docs/AltAz.php
# Example URL string:
# 'https://aa.usno.navy.mil/cgi-bin/aa_altazw.pl?form=1&body=10&year=2019&month=9&day=21&intv_mag=10&state=CA&place=Victorville'

UrlStr = 'https://aa.usno.navy.mil/cgi-bin/aa_altazw.pl?form=1&body=10&'
UrlStr = UrlStr + 'year=' + YY + '&month=' + MM + '&day=' + DD
UrlStr = UrlStr + '&intv_mag=' + str(Interval) + '&state=' + State + '&place=' + City

webUrl  = urllib.request.urlopen(UrlStr)

# print ("result code: " + str(webUrl.getcode()))
data = webUrl.read()

# print(data)

# print("\n\nData Length: {}\n\n".format(len(data)))

encoding = "utf-8"

Dt = data.decode(encoding)
Dlines = Dt.split('\n')

Dlist = []

# print('-' * 75, '\n\n')

with open("sunTrack.txt", 'w') as fid:
    for line in Dlines:
        if(':' in line and '<' not in line):
            fid.write(line)
            fid.write('\n')
#            print(line)
            tLine = line.split()
            HM = tLine[0].split(':')
            H, M = int(HM[0]), int(HM[1])
            Altitude = float(tLine[1])
            Azimuth = float(tLine[2])
            Dlist.append([H, M, Altitude, Azimuth])

# print('-' * 75, '\n\n')

# print('\n\n')

for D in Dlist:
    print(D)



