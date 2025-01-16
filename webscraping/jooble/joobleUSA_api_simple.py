# -*- coding: utf-8 -*-
"""
Jooble.ORG job post search using Jooble own API.
Note that this API gives access only to the USA job market... but that's huge!

https://jooble.org/api/about

More info about POST input and reply:
    https://help.jooble.org/en/support/solutions/articles/60001448238-rest-api-documentation
    
    you receive an API key, with this note:
        "Please note that API has a default limit of 500 requests. 
        If you want to increase the number of requests or have other questions, 
        please write to us in response to this letter. Best regards, Jooble Team"

The response (output) is not formatted just written to a JSON and a CVS file 
(printed on screen if required, now commented out). Files are saved in this app's folder.
    
@author: Josesan77
Created on Thu Jan 16 10:10:45 2025
"""

import http.client
import csv
import json 
country_code = "us" # country_code": 2 character country code 
host = country_code + '.jooble.org' #can be simplified to: host = 'jooble.org'
key = '<YOUR_API_KEY>' #' <YOUR_API_KEY>' #request an API key here: 

connection = http.client.HTTPConnection(host)
#request headers
headers = {"Content-type": "application/json"}
#json query
#"keywords": search terms for your preferred job, ""location": city/region
body = '{ "keywords": "Data Analyst", "location": "New York"}' 
connection.request('POST','/api/' + key, body, headers)
response = connection.getresponse()
if response.status != 200:
    print(response.status, response.reason, 'Failed. Check connection/API key')
else:
    response_text = response.read()
    response_json = response_text.decode('utf8').replace("'", '"')
    response_txt = response_text.decode('utf8').replace("'", '"')
    #print(response_json) # write to screen
    
    file_name_csv = 'jooble_usa_positions.csv' #save in the folder of this app
    file_name_json = 'jooble_usa_positions.json'
    
    with open(file_name_csv, 'w', newline = '', encoding='utf-8') as csv_file: #, newline = '\n') as csv_file:
        csv_writer = csv.writer(csv_file) #, quoting=csv.QUOTE_NONNUMERIC )
        csv_writer.writerow([response_json.replace('\\n','').replace('\\r','')]) #        
    csv_file.close() 
    with open(file_name_json, 'w') as f:
        json.dump(response_json, f)    
    f.close()   
    
    print('Jooble Positions data saved in files: {file_name_csv}, {file_name_json}')