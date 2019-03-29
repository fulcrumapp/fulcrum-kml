# This will only work with a csv from the downloader than contains a title field. 
# Will need to have csv, kml and this script in the same folder to run correctly. 
# Change the names of the files below.  New kml file will be called 'updated_kml.kml'


from fastkml import kml 
import csv
import sys
import getopt

fullCMDArguments = sys.argv

csvfile = fullCMDArguments[2]  # name of csv file
kmlfile = fullCMDArguments[4]  # name of kml file

fields = []
rows = []

with open(csvfile, 'r') as csvFile:
    csvreader = csv.reader(csvFile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

index = 0
for x in fields:
    if x == '_title':
        break
    index += 1

titles = []

for row in rows:
    titles.append(row[index])


with open(kmlfile, 'rt') as file:
    doc = file.read()

k = kml.KML()
k.from_string(doc)
features = list(k.features())
f2 = list(features[0].features())
f3 = list(f2[0].features())

index1 = 0
for x in f3:
    x.name = titles[index1]
    index += 1

file = open('updated_kml.kml', 'w')
file.write(k.to_string(doc))
file.close()