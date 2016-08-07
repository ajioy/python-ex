# py3.4

import urllib.request

url = "http://placekitten.com/200/300"
response = urllib.request.urlopen(url)
#the other way
#req = urllib.request.Request(url)
#response = urllib.urlopen(req)
cat_image = response.read()

with open("cat_200_300.jpg", "wb") as f:
    f.write(cat_image)
    f.close()
