text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text = 'Today is 5/6/2014. Python learning starts 3/13/2014.'
import re
res = re.sub(r"(\d+)/(\d+)/(\d+)", r'\3-\1-\2', text)
print(res)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
res = datepat.sub(r'\3-\1-\2', text)
print(res)

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{}-{}-{}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n)
