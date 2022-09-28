import pandas as pd
import time
import requests
import csv
import urllib3

SLEEP = 0

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

url = ["url"]
pid = ["pid"]
Status = []
inputfile = ['C:\\...urls.csv'] #enter the path to your input file
outputfile = ['C:\\...statuscodes.csv'] #enter the path to your outputfile

cols = ['pid', 'url', 'Status'] #define column headers
df = pd.read_csv('inputfile') #open input file
print(df)

#get the url status code
def url_access(x):
    try:
        return requests.head(x,timeout=5).status_code
    except:
        return -1

df['Status'] = df['url'].apply(url_access)

dfcount = df.groupby('Status')['url'].count().reset_index()

print(df)
df.to_csv('outputfile') #create outputfile with status codes

