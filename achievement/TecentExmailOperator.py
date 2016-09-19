#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = 'ajioy'
__create_data__ = '2016/9/8 16:10'
__py_version__ = '2.7.8'
__description__ = '用腾讯企业邮箱开放协议接口，实现按邮箱账号批量禁用、删除功能'

import urllib
import urllib2
import json

#   POST method
def postRequest(url, data):
    try:
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
    except Exception, e:
        print "error occur:", e
    finally:
        return the_page

#POST method access_token
#client_id yourmail@mail.com
#client_secret somesecretcode...
def getAccessToken():
    url = "https://exmail.qq.com/cgi-bin/token"
    values = {'grant_type': 'client_credentials', \
          'client_id': 'your admin account',
          'client_secret': 'your secretcode'}
    data = urllib.urlencode(values)
    the_page = postRequest(url, data)
     # get a json data  access_token
    jsonData = json.loads(the_page)
    return jsonData["access_token"] #json string


#   有关腾讯企业邮箱的操作封装类
class TecentExmailOperator(object):

    def __init__(self):
        self.__accesstoken = getAccessToken()
        self.__url = 'http://openapi.exmail.qq.com:12211/openapi/user/sync'

    # 统一操作功能
    def commonOperator(self, alias, opt, opentype = 0):
        data = {'access_token': self.__accesstoken,
                'action': opt,
                'alias': alias,
                'opentype':opentype
                }
        data_encode = urllib.urlencode(data)
        res = postRequest(self.__url, data_encode)
        if res != '':
            error = json.loads(res)
            return error['error']
        else:
            return 'done'

    # 根据邮箱账号删除，慎用，调用接口删除的账户无法通过系统日志模块恢复
    # 建议调用禁用功能，再手动选中删除，可在7天内恢复
    def delAccountByAlias(self, alias):
        opt = '1'   # DEL
        return self.commonOperator(alias, opt)

    # 实现禁用
    def forbidAccountByAlias(self, alias):
        opt = '3'   # MOD
        opentype = '2'
        return self.commonOperator(alias, opt, opentype)
    # 启用账号
    def enableAccountByAlias(self, alias):
        opt = '3'  # MOD
        opentype = '1'
        return self.commonOperator(alias, opt, opentype)

    def choice(self, nSel, alias):
        if nSel == 1:
            return self.delAccountByAlias(alias)
        elif nSel == 2:
            return self.forbidAccountByAlias(alias)
        elif nSel == 3:
            return self.enableAccountByAlias(alias)
        else:
            return None

#   测试用例
def main():

    nCur = 0
    nSuc = 0
    nFailed = 0

    try:
        # 手动输入源数据表，如alias.txt
        file_name = raw_input("input filename:")
        op = TecentExmailOperator()
        # 处理后的结果集
        fw = open(r"output.txt", 'w')
        nChoice = int(raw_input("what do u want to do?\n1.delete\n2.forbid\n3.enable\n"))
        print "--------------------result-----------------------"
        with open(file_name, 'r') as f:
            for line in f.readlines():
                alias = line.lstrip()
                alias = line.rstrip()
                nCur += 1
                if alias == '': # 空行
                    output = "(%d)\tempty line\n" % nCur
                    print output
                    fw.write(output)
                    continue
                res = op.choice(nChoice, alias)
                if res == 'done':
                    nSuc += 1
                elif res == 'user_not_found':
                    nFailed += 1
                else:
                    print "unknown error occur!"

                output = ("(%d)\t" % nCur) + alias + "\t" + res + "\n"
                print output
                fw.write(output)

    except IOError,e:
        print e

    finally:
        print "-------------------------------------------------"
        print "\t^-^ok,it's done!\r"
        print "\t> total:%d\r" % (nSuc + nFailed)
        print "\t> successful:%d\r" % nSuc
        print "\t> failed:%d\r" % nFailed
        print "-------------------------------------------------"


if __name__ == "__main__":
    main()
