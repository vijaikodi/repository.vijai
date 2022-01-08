import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
from urllib.parse import urlparse
from .unpack import unpack
from lib import playallu



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
    resp = requests.get(url, verify=False)
    html = resp.text
    data = re.compile(reg).findall(html)
    return data
def getredirectedurl(url):
    try:
        r= requests.get(url,verify=False)
        return r.url
    except Exception as e:
        Dialog().ok('XBMC', str(e))

# def resolve_arivakam(url):
#     try:
#         reg = '"file":\"(.*?)\"'
#         link1 = getdatacontent(url,reg)
#         link1 = link1[0]
#         link = getredirectedurl(link1)
#         link = link.split("?")
#         link = link[0]
#         t1 = urlparse(link)
#         t2 = t1.path
#         r = t1.path.split("/")[-2].split(",")[-1]
#         t3 = t2.split("/")
#         t3[-2] = r
#         r = "/".join(t3)
#         t=t1._replace(path=r)
#         link = t.geturl()
#         xbmc.log("----------------------------------------Arivakam----------------------------------------------------------------")
#         xbmc.log(link)
#         #['https://32vod-adaptive.akamaized.net/exp=1631566344~acl=%2Fd5994a51-6d0f-410c-8cab-f0e2b55704af%2F%2A~hmac=9ba5e07383d402bd8f10f4692eae6f169647905e44541f7e1f4d5b3d6aa9c5f6/d5994a51-6d0f-410c-8cab-f0e2b55704af/sep/video/589c9043,281f15ba,279905cd,43a500be/master.m3u8', 'absolute=1']
#         return link
#     except:
#         return None    

def resolve_arivakam(url):
    reg = '"file":\"(.*?)\"'
    resp = getdatacontent(url,reg)
    if resp:
        link = resp[0]
    else:
        reg = '<iframe id="embedvideo" src=\"(.*?)\"'
        resp = getdatacontent(url,reg)
        if resp:
            link = resp[0]
            movieurl = playallu.resolve_playallu(link)
            link = movieurl
    return link
