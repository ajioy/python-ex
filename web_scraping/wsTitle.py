# coding:GBK
# web scraping website title

'''
 utf-8 code will throw error:UnicodeDecodeError:\
 'utf-8' codec can't decode byte 0xcd in position 125:\
 invalid continuation byte
 GBK will be ok
'''

import urllib.request
import re

def wsTitle(urls):
    regex = r'<title>(.+?)</title>'
    pattern = re.compile(regex)
    i = 0
    while i < len(urls):
        htmlfile = urllib.request.urlopen(urls[i])
        htmltext = htmlfile.read().decode('GBK')
        title = re.findall(pattern, htmltext)
        
        print(title)
        #print(htmltext[0:100]) print 100 byte content
        i += 1

if __name__ == '__main__':
    urls = [r'http://www.163.com',r'http://www.qq.com', r'http://www.sohu.com']
    wsTitle(urls)


