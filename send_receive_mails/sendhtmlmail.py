# -*- coding:utf-8 -*-
__author__ = 'AjioyHome'
__date__ = '16-7-30 上午11:56'
__description__ = ' '

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

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr(u'python<%s>' % from_addr)
msg['To'] = _format_addr(u'recv<%s>' % to_addr)
msg['Subject'] = Header(u'html格式的邮件...', 'utf-8').encode()
tls_port = 587
server = smtplib.SMTP(smtp_server, tls_port)
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string() )
server.quit()
