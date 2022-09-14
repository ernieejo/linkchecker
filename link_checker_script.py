# status code checker
import requests
import csv
import time

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

SLEEP = 0 # Time in seconds the script should wait between requests
PID = []
PID_list = []
url_list = []
url_statuscodes = []
url_statuscodes.append(["PID","url","status_code"]) # set the file header for output


def getStatuscode(url):
    try:
        r = requests.head(url,verify=False,timeout=5) # it is faster to only request the header
        return (r.status_code)

    except:
        return -1

# Url checks from file Input
with open('urls.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        url_list.append(row[1])
        PID_list.append(row[0])

# Loop over full list
for PID in PID_list:
    print(PID)
    
for url in url_list:
    print(url)
    check = [PID,url,getStatuscode(url)]
    time.sleep(SLEEP)
    url_statuscodes.append(check)
    
# Save file
with open("urls_withStatusCode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(url_statuscodes)
