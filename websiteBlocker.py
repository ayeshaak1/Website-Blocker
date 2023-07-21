import time
from datetime import datetime as dt

# use =r to avoid path errors
hostsPath=r"C:\Windows\System32\Drivers\etc\hosts"
redirect="127.0.0.1"
# array of websites to block
websiteList={"www.agar.io", "agar.io", "www.instagram.com", "instagram.com"}

startTime = 8
endTime = 16

while True:
    # check 
    if dt(dt.now().year, dt.now().month, dt.now().day, startTime) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, endTime):
        print("Working hours")
    time.sleep(5)