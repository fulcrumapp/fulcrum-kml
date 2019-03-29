# Change the names of the files below.  New kml file will be called 'updated_kml.kml'
# Need API access from fulcrum and the Fulcrum pyhton library installed.
# This script and the kml file need to be in the same folder. 


from fastkml import kml
from fulcrum import Fulcrum
import sys
import getopt

fullCMDArguments = sys.argv


fulcrum = Fulcrum(key=fullCMDArguments[6])  # add API your API key 

kmlfile = fullCMDArguments[2] # name of kml file. 

with open(kmlfile, 'rt') as file:
    doc = file.read()

k = kml.KML()
k.from_string(doc)
features = list(k.features())
f2 = list(features[0].features())
f3 = list(f2[0].features())

# fieldKey can be updated to any title key, key or multiple keys within your form.  
# View the form definition by constructing the following URL and pasting it 
# into your browser:
# https://api.fulcrumapp.com/api/v2/forms/YOUR-FORM-ID.json?token=YOUR-API-KEY
# In the returned form definition JSON file, search for the key within form_values 
# and copy the value. If you want to display additional information in the name
# of your pins, make note of the key values that match up with the 
# labels corresponding to the fields you created in the app builder.


fieldKey = fullCMDArguments[4] # change to your field key.
for x in f3:
    record = fulcrum.records.find(x.name)
    x.name = record['record']['form_values'][fieldKey]

file = open('updated_kml.kml', 'w')
file.write(k.to_string(doc))
file.close()