import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
from .unpack import unpack
def getdatacontent_dict(url,reg):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    r = re.compile(reg)
    data = [m.groupdict() for m in r.finditer(html)]
    return data
def getdatacontent(url,reg):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    data = re.compile(reg).findall(html)
    return data
def getredirectedurl(url):
    try:
        r= requests.get(url,verify=False)
        return r.url
    except Exception as e:
        Dialog().ok('XBMC', str(e))

def resolve_arivakam(url):
    try:
        reg = '"file":\"(.*?)\"'
        link1 = getdatacontent(url,reg)
        link1 = link1[0]
        link = getredirectedurl(link1)
        return link
    except:
        return None    
