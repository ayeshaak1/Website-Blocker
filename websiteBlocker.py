import time
from datetime import datetime as dt

# use =r to avoid path errors
hostsPath=r"C:\Windows\System32\Drivers\etc\hosts"
redirect="127.0.0.1"
# array of websites to block
websiteList={"www.agar.io", "agar.io", "www.instagram.com", "instagram.com"}

while True:
    print(1)
    time.sleep(5)