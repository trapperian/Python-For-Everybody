# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1648937.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup("span")
count = 0
total = 0
for span in tags:
    total += int(span.contents[0])
    count += 1
    # Look at the parts of a tag
    # print('TAG:', span)
    # print('URL:', span.get('href', None))
    # print('Contents:', span.contents[0])
    # print('Attrs:', span.attrs)
print(total)
print(count)
