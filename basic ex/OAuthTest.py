import urllib
import urllib2
import base64
import json
import requests

#POST method access_token
#client_id yourmail@mail.com
#client_secret somesecretcode... 
def getAccessToken():
    url = "https://exmail.qq.com/cgi-bin/token"
# url = "http://openapi.exmail.qq.com:12211/openapi/user/get"
    values = {'grant_type': 'client_credentials', \
          'client_id': 'yourmail@mail.com',
          'client_secret': 'somecode'}
    data = urllib.urlencode(values)
    #print data

    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page  # get a json data  access_token
#json string
jStr = json.loads(getAccessToken())
AccessToken = jStr["access_token"]
#print getAcessToken()
print AccessToken

auth = 'Bearer' + base64.encodestring(AccessToken)[:-1]
print auth
data = {'alias':'yourmail@mail.com',
        'access_token':auth}
data_j = json.dumps(data) #trans to json
#data_j = urllib.urlencode(data)
# header = {"Host":"openapi.exmail.qq.com",
#           "Authorization":auth,#"Bearer:%s" % AccessToken,
#           "Content-length":len(data_j),
#           "Content-type":"application/x-www-form-urlencoded;charset=UTF-8"
#           }
url = 'http://openapi.exmail.qq.com:12211/openapi/user/get'
request = urllib2.Request(url,data_j)
req = urllib2.urlopen(request)
print req.read()
# r = requests.post(url, data_j)
# print r.text


''' select code and press ctrl+/ will comment
client_secret=somecode&grant_type=client_credentials&client_id=yourmail@mail.com
{
	"access_token":"some code",
	"token_type":"Bearer",
	"expires_in":432000,
	"refresh_token":""
}
'''


