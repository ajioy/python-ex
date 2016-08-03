#-*- coding=utf-8 -*-
__author__ = 'ajioy'
__create_data__ = '2016/7/26 15:59'
__description__ = ''

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
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

msg = MIMEText(u'这里是邮件内容,sent by python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python专家<%s>' % from_addr)
msg['To'] = _format_addr(u'亲爱的<%s>' % to_addr)
msg['Subject'] = Header(u'一封神秘的邮件', 'utf-8').encode()

tls_port = 587
server = smtplib.SMTP(smtp_server, tls_port)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()