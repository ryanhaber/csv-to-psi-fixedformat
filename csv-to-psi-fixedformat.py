import csv
import json
import sys

# get input and output files from commandline
inputfile = sys.argv[1]
outputfile = sys.argv[2]

# load the CSV, convert it to json, then build a python dictionary from the json
csvfile = open(inputfile)
table = csv.reader(csvfile)

output = open(outputfile, "w")
output.seek(0)

fixedformat = "%-20s%-20s%-2s%-10s%-40s%-40s%-14s%-2s%-9s%-10s%-10s%-8s%-2s%-7s%-1s%-8s%-2s%-1s%-1s%-1s%-1s%-1s%-2s%-20s%-2s%-10s%-40s"

for row in table:
	datas = tuple(row)
	output.write( fixedformat % datas )

output.close()