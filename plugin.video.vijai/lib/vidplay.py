import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
from urllib.parse import urlparse
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

def resolve_vidplay(url,source):
    #web_pdb.set_trace()
    url = url.replace("embed7","xembed")
    headers = {
        'authority': 'vidplay.one',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://tamilvip.live/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    response = requests.get(url=url, headers=headers)
    reg = '{file:\"(.*?)\"}'
    html = response.text
    data = re.compile(reg).findall(html)
    if data:
        streamurl = []
        for item in data:
            if 'label' in item:
                temp= []
                url = item.split(',')
                temp.append(url[0])
                temp.append(url[1])
                streamurl.append(temp)
            else:
                temp = []
                title = 'm3u8-stream link'
                temp.append(item)
                temp.append(title)
                streamurl.append(temp)

        return streamurl
    else:
        return None