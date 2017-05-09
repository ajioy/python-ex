# 不懂
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# 清理空白字符
remap = {
        ord('\t') : ' ',
        ord('\f') : ' ',
        ord('\r') : None 
}

a = s.translate(remap)
print(a)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))
