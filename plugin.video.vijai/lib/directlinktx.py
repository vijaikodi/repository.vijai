import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
from urllib.parse import urlparse,unquote
from .unpack import unpack
from lib import playallu
from xbmcgui import ListItem, Dialog
import web_pdb
import resolveurl as urlresolver
import six


def check_hosted_media(vid_url):
    from resolveurl import HostedMediaFile
    return HostedMediaFile(url=vid_url)

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
    return data
def getredirectedurl(url):
    try:
        r= requests.get(url,verify=False)
        return r.url
    except Exception as e:
        Dialog().ok('XBMC', str(e))

def resolve_directlinktx(url):
    #web_pdb.set_trace()
    reg = 'class=\"main-button\sdlbutton\"\shref=\"(.*?)\"'
    data = getdatacontent(url,reg)
    if data:
        data = data[0]
        if "videoemx2" in data:
            url = data
            reg = 'iframe\ssrc=\"(.*?)\"'
            url = getdatacontent(url,reg)
            if url:
                url = url[0]
                hmf = check_hosted_media(url)
                if not hmf:
                    Dialog().ok('Indirect hoster_url not supported by smr: {0}'.format(url), 'Resolve URL')
                    return False
                try:
                    #web_pdb.set_trace()
                    stream_url = hmf.resolve()
                    #return stream_url
                    # If resolveurl returns false then the video url was not resolved.
                    if not stream_url or not isinstance(stream_url, six.string_types):
                        if not stream_url:
                            msg = 'File removed'
                        else:
                            msg = str(stream_url)
                        Dialog().notification('XBMC',msg)
                        return False
                except Exception as e:
                    try:
                        msg = str(e)
                    except:
                        msg = url
                        Dialog().ok(msg, 'Resolve URL', 5000)
                    return False
                return stream_url
        else:
            try:
                movieurl = urlresolver.HostedMediaFile(data) 
                movieurl = movieurl.resolve()
                return movieurl
            except Exception as e:
                Dialog().ok('XBMC', str(e)) 

