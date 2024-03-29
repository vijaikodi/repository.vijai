import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests,xbmcplugin,xbmcgui,xbmcvfs
import resolveurl as urlresolver
from .unpack import unpack


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

def get_redirect_url(url, headers={}):
    request = urllib.request.Request(url, headers=headers)
    request.get_method = lambda: 'HEAD'
    response = urllib.request.urlopen(request)
    return response.geturl()

def play_video(path):
    """
    Play a video by the provided path.
    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(plugin.handle, True, listitem=play_item)


def resolve_playallu(url):
    #web_pdb.set_trace()
    reg = 'idfile\s=\s\"(.*?)\";\s+var\sidUser\s=\s\"(.*?)\";'
    data = getdatacontent(url,reg)
    data = data[0]
    url = 'https://api-plhq.playallu.xyz/apiv4/'+str(data[1])+'/'+str(data[0])
    headers = {
        'authority': 'api-plhq.playallu.xyz',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://play.playallu.xyz',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://play.playallu.xyz/',
        'accept-language': 'en-US,en;q=0.9',
    }
    r = requests.get('https://tamilgun.com')
    domain = r.url
    from urllib.parse import urlparse
    domain = urlparse(domain).netloc
    xbmc.log(domain)
    data = {
      'referrer': 'https://'+domain,
      'typeend': 'html'
    }

    response = requests.post(url, headers=headers, data=data)
    data1 = response.json()
    data = response.text
    tgdr = str(data1["tgdr"])
    reg = '\"(.*?)\"'
    data = re.compile(reg).findall(data)
    data =  (data[7:])
    fpath = xbmcvfs.translatePath('special://temp')
    fpath = fpath + "test.m3u8"
    f = open(fpath, "w")
    f.write("#EXTM3U\n")
    f.write("#EXT-X-VERSION:3\n")
    f.write("#EXT-X-TARGETDURATION:"+tgdr+"\n")
    f.write("#EXT-X-PLAYLIST-TYPE:VOD\n")
    for line in data:
        f.write("#EXTINF:"+tgdr+",\n")
        #f.write("https://plhq01.ggccallu001.xyz/stream/v5/"+line+".html\n")
        f.write("https://plhq01.strplhqallu001.click/stream/v5/"+line+".html\n")
    f.write("#EXT-X-ENDLIST\n")
    f.close()
    return fpath
