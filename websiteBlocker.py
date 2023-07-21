import time
from datetime import datetime as dt

hostsTemp="hosts"
# use =r to avoid path errors
hostsPath=r"C:\Windows\System32\Drivers\etc\hosts"
redirect="127.0.0.1"
# array of websites to block
websiteList=["www.agar.io", "agar.io", "www.instagram.com", "instagram.com"]

startTime = 8
endTime = 18

while True:
    # check if between working hours
    if dt(dt.now().year, dt.now().month, dt.now().day, startTime) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, endTime):
        print("Working hours")
        # open to read and write
        with open(hostsTemp, 'r+') as file:
            # store the entire file in content
            content=file.read()

            # check if website is already in file
            for website in websiteList:
                if website in content:
                    pass
                # if its not, add website
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Outside of working hours")
    time.sleep(5)