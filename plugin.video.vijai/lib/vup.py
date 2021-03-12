import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
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

def resolve_vup(url):
    reg = "<script type='text\/javascript'>eval(.*?)\s+<\/script>"  
    out = getdatacontent(url,reg)
    out = unpack(out[0])
    reg = 'sources:\s*\[{src:\s*"(?P<url>[^"]+)'
    url = re.compile(reg).findall(out)
    url = url[0]
    return url