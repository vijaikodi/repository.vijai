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
    headers = {
    'authority': 'ww5.vcdnlare.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://ww7.5movierulz.pet/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    resp = requests.get(url,headers=headers,verify=False)
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
def getdatacontentvcdnx(url,reg):
    headers = {
        'authority': 'hls2.vcdnx.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        #'if-modified-since': 'Tue, 02 Jan 2024 07:06:21 GMT',
        'origin': 'https://ww5.vcdnlare.com',
        'referer': 'https://ww5.vcdnlare.com/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    resp = requests.get(url,headers=headers)
    html = resp.text
    xbmc.log(html)
    data = re.compile(reg).findall(html)
    return data

def resolve_vcdnlare(url,source):
    #web_pdb.set_trace()
    url = url.replace("#038;","")
    url = url + "&autoplay=1"
    reg = '<script[\s\S]*?>[\s\S]*?<\/script>'
    data = getdatacontent(url,reg)
    if data:
        for item in data:
            if "eval(function" in item:
                try:
                    data1=unpack(item)
                    reg = "file\\\\\\\':\\\\\\\'(.*?)\'"
                    url = re.compile(reg).findall(data1)
                    url = url[0]
                    url = url[:-1]
                    urlsubstring = url.split("/")
                    reg = "(.*?)\?ts=\d+"
                    data = getdatacontentvcdnx(url,reg)
                    data = data[0]
                    url = "https://"+urlsubstring[2]+"/hls/"+urlsubstring[4]+"/"+data+"?ts=20"
                    return url
                except:
                    Dialog().ok('XBMC', 'Unable to locate video')
    else:
        return None
