import csv
from datetime import datetime
from dateutil.parser import parse
import re

def parseHms(s):
	m = re.search(r"(\d+):(\d+):(\d+)", s).groups()
	return { "hours": int(m[0]), "minutes": int(m[1]), "seconds": int(m[2])}

def hmsToSeconds(hms):
	return hms["seconds"] + hms["minutes"]*60 + hms["hours"]*3600

def secondsToHms(s):
	hours = int(s / 3600)
	r1 = s % 3600
	minutes = int(r1 / 60)
	seconds = r1 % 60
	return { "hours": hours, "minutes": minutes, "seconds": seconds}

def addTime(t1, t2):
	s1 = hmsToSeconds(t1)
	s2 = hmsToSeconds(t2)
	return secondsToHms(s1 + s2)

with open('c4-time-tracking.csv') as csv_file:
  csvr = csv.reader(csv_file)
  headers = next(csvr, None)
  grandTotal = 0
  total = 0
  for r in csvr:
  	s = hmsToSeconds(parseHms(r[1]))
  	grandTotal += s
  	if r[2] == "yes":
  		total += s
  print(f"Grand total: {secondsToHms(grandTotal)}")
  print(f"Judged total: {secondsToHms(total)}")



