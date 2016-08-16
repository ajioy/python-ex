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

def getIps(html):
    p = r'(?:(?:[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:[01]?\d\d|2[0-4]\d|25[0-5])'
    ipLst = re.findall(p, html)

    for each in ipLst:
        print(each)
        

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/'
    getIps(openurl(url))
    
    
