import pandas as pd
import time
import requests
import csv
import urllib3

SLEEP = 0

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

url = ["URL"]
pid = ["pid"]
Status = []


df = pd.read_csv('C:\\...\\LinkChecker\\urls.csv')
cols = ['pid', 'URL', 'Status']
print(df)

def url_access(x):
    try:
        return requests.head(x,timeout=5).status_code
    except:
        return -1

df['Status'] = df['URL'].apply(url_access)

dfcount = df.groupby('Status')['URL'].count().reset_index()

print(df)
df.to_csv('C:\\...outputfile.csv')

