# -*- coding:utf-8 -*-
__author__ = 'AjioyHome'
__date__ = '16-7-30 下午5:24'
__description__ = ' '

from email.header import Header
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.utils import parseaddr, formataddr
from email import encoders
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((\
        Header(name, 'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr, unicode) else addr
    ))


from_addr = 'from@gmail.com'
password = 'your password'
to_addr = 'to@gmail.com'
smtp_server = 'smtp.gmail.com'

msg = MIMEMultipart()
msg['From'] = _format_addr(u'python<%s>' % from_addr)
msg['To'] = _format_addr(u'recv<%s>' % to_addr)
msg['Subject'] = Header(u'带附件的邮件...', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText(u'<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
filename_pic = u'test1.jpg' #出现中文名会有问题
with open(filename_pic, 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename=filename_pic)
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=filename_pic)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

tls_port = 587
server = smtplib.SMTP(smtp_server, tls_port)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string() )
server.quit()
