import urllib.request, urllib.error, urllib.parse,re,urllib.request,urllib.parse,urllib.error,requests
import resolveurl as urlresolver
from .unpack import unpack
import web_pdb

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


def resolve_viralweb8(url,source):
    #web_pdb.set_trace()
    if 'master.txt' in url:
        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'origin': 'https://www.jimkimble.com',
                'priority': 'u=1, i',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }
        response = requests.get(url, headers=headers)
        data = response.text
        reg = r"NAME=\"(?P<quality>.*?)\",(.*?),AUDIO=\"audio\"\s(?P<url>.*?)$"
        r = re.compile(reg)
        data = [m.groupdict() for m in r.finditer(data)]
        return data
    if 'authenticator' in url:
        response = requests.get(url)
        url = response.text
        item = []
        data = {}
        data['quality'] = "Auto"
        data['url'] = url
        item.append(data)
        return item