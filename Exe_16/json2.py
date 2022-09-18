import json
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"
html = urlopen(url, context=ctx).read()

info = json.loads(html)
print("Comments:", info['comments'])
