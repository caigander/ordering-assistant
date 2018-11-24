#import math, urllib
from login import o_user, o_pass, o_url

print(o_user)
print(o_pass)
print(o_url)

"""
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'j_username' : username, 'j_password' : password})
opener.open('http://orders.coppercanyonfarms.com/muir/Login.aspx', login_data)
resp = opener.open('https://website.com/hiddenpage')

print resp.read()
"""
