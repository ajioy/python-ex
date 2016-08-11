#-*- coding=utf-8 -*-
__author__ = 'ajioy'
__create_data__ = '2016/8/8 12:25'
version__ = '3.5'
__description__ = ''

import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
iplist = ['122.96.59.102:80', '116.30.155.192:8888']
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
