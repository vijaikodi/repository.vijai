import urllib2,re,xbmc,urllib,requests
def getdatacontent(url,reg):
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    req = urllib2.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read()
    data = re.compile(reg).findall(html)
    return data

def resolve_videobin(url):  
    reg = 'sources\s*:\s*\[(.+?)\]'
    streamurl = getdatacontent(url,reg)
    streamurl = streamurl[0]
    streamurl = streamurl.split('","')
    streamurl = streamurl[1]
    return streamurl