# First, lock up your host file
# On Windows C:\Windows\System32\drivers\etc
# Open host file with a text editor

import time
from datetime import datetime as dt

# As the backslashed could be misinterpreted by Python e.g. \n
# the r is addded to tell Python we are passing a raw string
#real path
#hostpath = r'C:\Windows\System32\drivers\etc\hosts'
# testing path
hostpath = r"C:\Users\Katja\PythonCodingTraining\WebsiteBlocker\hosts_test"


# IP where browser will be redirected to
redirect = '120.0.0.1'

#List of website that will be blocked
blockedwebsites = ['https://rosebakes.com/carnival-cruise-warm-chocolate-melting-cake/', 
                'https://elavegan.com/vegan-lava-cake-gluten-free/']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        with open(hostpath, 'r+') as hostfile:
            content = hostfile.read()
            print(content)
            for website in blockedwebsites:
                if website in content:
                    pass
                else:
                    hostfile.write(redirect + ' '+ website + '\n')
    else:
        with open(hostpath, 'r+') as hostfile:
            # readlines() produces a list with all the lines in the file
            content = hostfile. readlines()
            # Placing the cursor before first character of file content
            hostfile.seek(0)
            # looping through each line of the host file
            for line in content:
                if not any(website in line for website in blockedwebsites):
                    hostfile.write(line)
            # Everything after the cursor will be deleted
            hostfile.truncate()
    time.sleep(10) 
