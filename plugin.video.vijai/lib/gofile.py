import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests,json
from .unpack import unpack
def getdatacontent(url,reg):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    data = re.compile(reg).findall(html)
    return data

def resolve_gofile(url):
    url = url.split('/')
    param =  url[-1]
    tempurl = "https://apiv2.gofile.io/getServer?c="
    url = tempurl+param
    response = requests.get(url)
    serv = json.loads(response.text)
    test = serv['data']
    serv = test['server']
    url = 'https://'+serv+'.gofile.io/getUpload?c='+param
    response = requests.get(url)
    url = json.loads(response.text)
    url = url['data']
    url = url['files']
    reg = "'link':\s+u'(.*?)'"
    url = str(url)
    data = re.compile(reg).findall(url)
    data = data[0]
    return data
