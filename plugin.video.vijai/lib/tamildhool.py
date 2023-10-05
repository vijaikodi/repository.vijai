import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
from urllib.parse import urlparse,unquote
from .unpack import unpack
from lib import playallu
from xbmcgui import ListItem, Dialog
import web_pdb
import resolveurl as urlresolver

def getcontent(url):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    return html

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
    resp = requests.get(url,verify=False)
    html = resp.text
    xbmc.log(html)
    data = re.compile(reg).findall(html)
    xbmc.log(str(data))
    return data
def getredirectedurl(url):
    try:
        r= requests.get(url,verify=False)
        return r.url
    except Exception as e:
        Dialog().ok('XBMC', str(e))

def resolve_tamilray(url):
    #web_pdb.set_trace()
    reg = 'src=\"(.*?)\?'
    url = url.replace("&#038;","&")
    data = getdatacontent(url,reg)
    if data:
        streamurl = data[0]
        try:
            movieurl = urlresolver.HostedMediaFile(streamurl)
            movieurl = movieurl.resolve()
            return movieurl
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    else:
        return None
