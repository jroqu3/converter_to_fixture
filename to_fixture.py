import sys
import getopt
import csv
import os
from os.path import dirname
import simplejson

try:
    script, input_file_name, model_name = sys.argv
except ValueError:
    print ("\nRun via:\n\n%s input_file_name model_name" % sys.argv[0])
    print ("\ne.g. %s airport.csv app_airport.Airport" % sys.argv[0])
    print ("\nNote: input_file_name should be a path relative to where this script is.")
    sys.exit()

PATH_FILE = '/tmp/peppol/'

if not os.path.exists(PATH_FILE):
    os.makedirs('/tmp/peppol/')

in_file =  dirname(__file__) + input_file_name
out_file = PATH_FILE + input_file_name.split('/')[-1].split('.')[0] + '.json'

print ("'************ CONVERTING %s FROM CSV TO JSON AS %s '************" % (in_file, out_file))

f = open(in_file, 'r' )
fo = open(out_file, 'w')

reader = csv.reader( f )

header_row = []
entries = []
pk = 1 #row[0]
for row in reader:
    if not header_row:
        header_row = row
        continue
        
    model = model_name
    fields = {}
    for i in range(len(row)):
        active_field = row[i]
        fields[header_row[i]] = active_field.strip()

    row_dict = {}
    row_dict["pk"] = pk #int(pk)
    row_dict["model"] = model_name
    
    row_dict["fields"] = fields
    entries.append(row_dict)
    pk += 1

fo.write("%s" % simplejson.dumps(entries, indent=4))
f.close()
fo.close()

print("'************ FILE CONVERTED ************")