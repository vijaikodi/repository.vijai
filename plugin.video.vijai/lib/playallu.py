import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests,xbmcplugin,xbmcgui,xbmcvfs
import resolveurl as urlresolver
from .unpack import unpack
import base64
import six
from six.moves import urllib_parse
from lib import client
import web_pdb
import json

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

#obselete since 28/09/2024
# def resolve_playallu(url):
#     #web_pdb.set_trace()
#     reg = 'idfile\s=\s\"(.*?)\";\s+var\sidUser\s=\s\"(.*?)\";'
#     data = getdatacontent(url,reg)
#     data = data[0]
#     url = 'https://api-plhq.playallu.xyz/apiv4/'+str(data[1])+'/'+str(data[0])
#     headers = {
#         'authority': 'api-plhq.playallu.xyz',
#         'pragma': 'no-cache',
#         'cache-control': 'no-cache',
#         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
#         'accept': '*/*',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'sec-ch-ua-mobile': '?0',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
#         'sec-ch-ua-platform': '"Windows"',
#         'origin': 'https://play.playallu.xyz',
#         'sec-fetch-site': 'same-site',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-dest': 'empty',
#         'referer': 'https://play.playallu.xyz/',
#         'accept-language': 'en-US,en;q=0.9',
#     }
#     r = requests.get('https://tamilgun.com')
#     domain = r.url
#     from urllib.parse import urlparse
#     domain = urlparse(domain).netloc
#     xbmc.log(domain)
#     data = {
#       'referrer': 'https://'+domain,
#       'typeend': 'html'
#     }

#     response = requests.post(url, headers=headers, data=data)
#     data1 = response.json()
#     data = response.text
#     tgdr = str(data1["tgdr"])
#     reg = '\"(.*?)\"'
#     data = re.compile(reg).findall(data)
#     data =  (data[7:])
#     fpath = xbmcvfs.translatePath('special://temp')
#     fpath = fpath + "test.m3u8"
#     f = open(fpath, "w")
#     f.write("#EXTM3U\n")
#     f.write("#EXT-X-VERSION:3\n")
#     f.write("#EXT-X-TARGETDURATION:"+tgdr+"\n")
#     f.write("#EXT-X-PLAYLIST-TYPE:VOD\n")
#     for line in data:
#         f.write("#EXTINF:"+tgdr+",\n")
#         #f.write("https://plhq01.ggccallu001.xyz/stream/v5/"+line+".html\n")
#         f.write("https://plhq01.strplhqallu001.click/stream/v5/"+line+".html\n")
#     f.write("#EXT-X-ENDLIST\n")
#     f.close()
#     return fpath


def resolve_playallu(eurl, referer):
    referer = urllib.parse.unquote_plus(referer)
    from lib import jscrypto
    import binascii
    import hashlib

    def pencode(c, m):
        i = jscrypto.encode(c, m)
        f = base64.b64decode(i)
        i = binascii.hexlify(f)
        return six.ensure_str(i)

    def pdecode(i, f):
        y = binascii.unhexlify(i)
        b = base64.b64encode(y)
        k = jscrypto.decode(b, f)
        return k

    #headers = self.hdr
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
    refurl = urllib_parse.urljoin(referer, '/')
    pref = urllib_parse.urljoin(eurl, '/')
    headers.update({'Referer': refurl})
    epage = client.request(eurl, headers=headers)
    if isinstance(epage, six.binary_type) and six.PY3:
        epage = epage.decode('latin-1')

    idfile_enc = re.findall(r'''idfile_enc\s*=\s*["']([^"']+)''', epage)[0]
    iduser_enc = re.findall(r'''idUser_enc\s*=\s*["']([^"']+)''', epage)[0]
    curl = re.findall(r'''DOMAIN_API_Info\s*=\s*["']([^"']+)''', epage)[0]
    apiurl = re.findall(r'''DOMAIN_API\s*=\s*["']([^"']+)''', epage)[0]

    headers.update({'Referer': pref, 'Origin': pref[:-1]})
    c = json.loads(client.request(curl, headers=headers))

    idfile_dec = pdecode(idfile_enc, 'jcLycoRJT6OWjoWspgLMOZwS3aSS0lEn')
    iduser_dec = pdecode(iduser_enc, 'PZZ3J3LDbLT0GY7qSA5wW5vchqgpO36O')
    ctime_dec = pdecode(c.get('time'), 'vp0DGD9E5rp6X0a3QYZ1qbDpilL83FO7')
    cip_dec = pdecode(c.get('ip'), 'vp0DGD9E5rp6X0a3QYZ1qbDpilL83FO7')
    pdata = {
        "idfile": idfile_dec,
        "iduser": iduser_dec,
        "domain_play": refurl[:-1],
        "platform": "Win32",
        "ip_clien": cip_dec,
        "time_request": ctime_dec,
        "hlsSupport": True
    }
    z = pencode(json.dumps(pdata), 'vlVbUQhkOhoSfyteyzGeeDzU0BHoeTyZ')
    w = binascii.hexlify(hashlib.md5(six.ensure_binary(z + 'KRWN3AdgmxEMcd2vLN1ju9qKe8Feco5h')).digest())
    data = {'data': z + '|' + six.ensure_str(w)}
    jd = json.loads(client.request(apiurl, headers=headers, post=data))
    mfile = pdecode(jd.get('data'), 'oJwmvmVBajMaRCTklxbfjavpQO7SZpsL')

    # url = https://m3u8-play-270224.playallu.xyz/m3u8/type1-pl/6143ecfbe5b2952eb486ea18/66f6fc9d83bc463490f2a76f/1727539354/d99d1d4a70075beca58f0fb70e5bd43c

    headers = {
    'Accept': '*/*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'en-US,en;q=0.9',
    'Connection':'keep-alive',
    'Host':urllib.parse.urlparse(mfile).netloc,
    'Origin':'https://play.playallu.xyz',
    'Referer':'https://play.playallu.xyz/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':"Windows",
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    response = requests.get(mfile, headers=headers)
    web_pdb.set_trace()
    #need to clean the data received
    data = response.content
    data = data.decode("utf-8",errors='ignore')
    fpath = xbmcvfs.translatePath('special://temp')
    fpath = fpath + "test.m3u8"
    f = open(fpath, "w")
    for line in data:
         f.write(line)
    f.close()
    return fpath

    #return mfile + '|' + urllib_parse.urlencode(headers)