import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"
html = urlopen(url, context=ctx).read()

tree = ET.fromstring(html)
lst = tree.findall('comments/comment')
total = 0
for item in lst:
    total += int(item.find('count').text)

print('The total is: ' + str(total))
