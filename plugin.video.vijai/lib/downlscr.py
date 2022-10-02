import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
def getdatacontent(url,reg):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    data = re.compile(reg).findall(html)
    return data

def resolve_downlscr(url):  
    reg = '<iframe loading="lazy" src=\"(.*?)\"'
    streamurl = getdatacontent(url,reg)
    url = streamurl[0]
    print (url)
    reg = "document\.getElementById\(\'robotlink\'\)\.innerHTML\s(.*?)\.substring"
    tempurl = getdatacontent(url,reg)
    tempurl = tempurl[0]
    print (tempurl)
    reg = "id=(.*?)&expires=(.*?)&ip=(.*?)&token=(.*?)'"
    r = re.compile(reg)
    data = re.compile(reg).findall(tempurl)
    data = data[0]
    url = "https://shavetape.cash/get_video?id="+data[0]+"&expires="+data[1]+"&ip="+data[2]+"&token="+data[3]+"&stream=1"
    response = requests.head(url)
    return response.headers["location"]