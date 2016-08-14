import urllib.request
import os
'''
url = 'http://ww1.sinaimg.cn/mw600/005vbOHfgw1f6r66my7q5j30m80etjs4.jpg'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
response = urllib.request.urlopen(req)
html = response.read()

with open('girls.jpg', 'wb') as f:
    f.write(html)
    f.close()
'''
#本程序可用，问题有两个：
#一是ip容易被禁，返回503错误。二是页面地址并不一规律，2091,2089.2087....

def url_open(url):
    '''ip代理
    ipaddr = '101.201.235.141:8000'
    proxy_support = urllib.request.ProxyHandler({'http' : ipaddr})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    '''
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 \
    Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b =  html.find(']', a)

    #print(html[a:b])
    return html[a:b]

def find_imgs(url): #找到页面里的所有图片地址
    html = url_open(url).decode('utf-8')
    img_addrs = []
    
    a = html.find('img src="http://ww')

    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9

        a = html.find('img src="http://ww', b)

    for each in img_addrs:
       print(each)
    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        img = url_open(each)
        with open(filename, 'wb') as f:
            f.write(img)

def download_mm(folder = 'ooxx17', pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        print(page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()


