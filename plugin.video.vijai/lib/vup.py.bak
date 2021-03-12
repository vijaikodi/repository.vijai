import urllib2,re,xbmc,urllib,requests
from unpack import unpack
def getdatacontent(url,reg):
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    req = urllib2.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read()
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