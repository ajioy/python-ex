# coding:utf-8

import urllib.request
import re

def openurl(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 \
    (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def getImgs(html):
    p = r'<img class="BDE_Image".*?src="([^"]+\.jpg)'
    imgLst = re.findall(p, html)

    for each in imgLst:
        #print(each)
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)
        

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/4427944924'
    getImgs(openurl(url))
    
    
