import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = input("Which link position? ")
repeats = input("How many times? ")

position_int = int(position) - 1
repeats_int = int(repeats) - 1
# Retrieve all of the anchor tags
tags = soup("a")
print(tags[position_int].contents[0])
i = 0
while i < repeats_int:
    url = tags[position_int].get("href", None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    print(tags[position_int].contents[0])
    i += 1
