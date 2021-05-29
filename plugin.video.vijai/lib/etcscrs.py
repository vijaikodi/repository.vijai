import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
import resolveurl as urlresolver
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

def getcontent(url):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    return html

# def resolve_streamtape(url):
#     reg ='<iframe src="(.*?)"'
#     url = getdatacontent(url,reg)
#     url = url[0]
#     # reg = '"videolink"[^>]+>([^<]+)'
#     # url = getdatacontent(url,reg)
#     # url = url[0]
#     # url = 'http:'+url
#     movieurl = urlresolver.HostedMediaFile(url)
#     movieurl = movieurl.resolve()
#     return movieurl

def resolve_etcscrs(url):
    reg ='<iframe src="(.*?)"'
    url = getdatacontent(url,reg)
    return url[0]
    # html = getcontent(url)
    # reg = "innerHTML\s=\s\"\/\/streamtape\.to\/get_\"\s\+\s\'(.*?)\'"

    # # reg = '"videolink"[^>]+>([^<]+)'
    # # url = getdatacontent(url,reg)
    # # url = url[0]
    # # url = 'http:'+url
    # url = "https://streamtape.to/get_"

    # movieurl = urlresolver.HostedMediaFile(url)
    # movieurl = movieurl.resolve()
    # return movieurl