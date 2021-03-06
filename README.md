# fulcrum-kml

A library for changing pin names of kml files produced in Fulcrum. 

There are two approaches you can take to rename a pin's name from a Fulcrum id.  

## CSV-KML

Uses a csv file with the title of a record to update the kml pin name.  

### Requirements

Requires a kml file from Fulcrum and a csv file from Fulcrum from the Downloader.
The csv file must include the title column.  

### Usage

The python script, kml file, and csv file will need to be in the same folder.  

Run the script from terminal with `python csvkmlscript.py --csvfile 'csv-file.csv' --kmlfile 'kml-file.kml'`


## API-KML

Uses the fulcrum python api to retrieve the value of a field and update the kml pin name. 

[fulcrum-python](https://github.com/fulcrumapp/fulcrum-python) needs to be installed.  Install it with `pip install fulcrum`

[fastkml](https://fastkml.readthedocs.io/en/latest/installing.html) needs to be installed. Install it with `pip install fastkml`

Requires a kml file from Fulcrum.  

### Usage

Run the script from terminal with `python apikmlscript.py --input file-name.kml --field-key '####' --api-key 'your-api-key'`

 


