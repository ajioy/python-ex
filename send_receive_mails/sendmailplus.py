#-*- coding=utf-8 -*-
__author__ = 'ajioy'
__create_data__ = '2016/7/27 16:47'
__description__ = ''

import smtplib
from email import encoders

from email.header import Header
from email.MIMEBase import MIMEBase  #此方式或以下方式引入均可
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr #解析和格式化地址

# 格式化地址
def _format_addr(s):
    name, addr = parseaddr(s) #元组 切割出名称和地址
    return formataddr((\
        Header(name, 'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'from@gmail.com'
password = 'your password'
to_addr = 'to@gmail.com'
smtp_server = 'smtp.gmail.com'

#msg = MIMEText('哈喽，这是一个测试程序，自动发送邮件，仅供娱乐','plain','utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr(u'python专家<%s>' % from_addr)
msg['To'] = _format_addr(u'大师<%s>' % to_addr)
msg['Subject'] = Header(u'带图片或带附件的邮件...', 'utf-8').encode()

#msg.attach(MIMEText(u'这是正文，带图片的邮件哦', 'plain', 'utf-8'))
msg.attach(MIMEText(u'<html><body><h1>hello</h1>' +
                    '<p><img src="cid:0"?></p>' +
                    '</body></html>', 'html', 'utf-8'))
imagefile = 'test.jpg'
with open(imagefile, 'rb') as file:
    mime = MIMEBase('image', 'jpg', filename = imagefile)
    mime.add_header('Content-Disposition', 'attachment', filename = imagefile)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(file.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 587) #581 support ssl
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
