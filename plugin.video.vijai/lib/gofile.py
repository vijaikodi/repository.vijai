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
    apiurl = "https://api.gofile.io/getUpload?c="+param
    reg = '"link":\"(.*?)\"'
    url = getdatacontent(apiurl,reg)
    if url:
        return url[0]
    else:
        return None
        
