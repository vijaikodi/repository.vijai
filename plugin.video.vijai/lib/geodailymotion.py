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

def resolve_geodailymotion(url):
    #web_pdb.set_trace()
    #url = "https://geo.dailymotion.com/player/xaho6.html?video=k2blQ7nsDIkZNPzzxeN"
    reg = 'player\/(?P<playerid>.*?).html\?video=(?P<code>.*)'
    r = re.compile(reg)
    data = [m.groupdict() for m in r.finditer(url)]
    data = data[0]
    playerid = data['playerid']
    code = data['code']
    url = 'https://www.dailymotion.com/player/metadata/video/'+code
    # cookies = {
    # 'dmvk': '653153de42315',
    # 'ts': '256288',
    # 'v1st': 'db567921-f60d-42f8-aa9a-6182e21d5e7c',
    # 'usprivacy': '1---',
    # }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'dmvk=653153de42315; ts=256288; v1st=db567921-f60d-42f8-aa9a-6182e21d5e7c; usprivacy=1---',
        'Origin': 'https://geo.dailymotion.com',
        'Referer': 'https://geo.dailymotion.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'geo': '1',
        'player-id': playerid,
        'locale': 'en-US',
        'is_native_app': '0',
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
    )

    t = response.json()
    movieurl = t['qualities']['auto'][0]['url']
    if movieurl:
        return movieurl
    else:
        return None


