import urllib.request, urllib.error, urllib.parse,re,xbmc,urllib.request,urllib.parse,urllib.error,requests
# def resolve_embedtamilgun(url):
#     if "embed1.tamildbox" in url:
#         #xbmc.log("---------------------------------------embed1-tamildbox-----------------------------------------------------------")
#         if "https" in url:
#             url = url.replace("https","http")
#         elif "http" in url:
#             url = url
#         else:
#             url = 'http:'+url
#         proxy_handler = urllib2.ProxyHandler({})
#         opener = urllib2.build_opener(proxy_handler)
#         req = urllib2.Request(url)
#         opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#         r = opener.open(req)
#         html1 = r.read()
#         movieurl= re.compile("domainStream = '(.*?)'").findall(html1)
#         xbmc.log("---------------------------------------embed1-tamildbox - movie-url-----------------------------------------------------------")
#         xbmc.log(str(movieurl))
#         if movieurl:
#             for tempurl in movieurl:
#                 if tempurl:
#                     xbmc.log("---------------------------------------embed1-tamildbox - temp-url-----------------------------------------------------------")
#                     xbmc.log(tempurl)
#                     return tempurl
#         elif "domainStream = domainStream.replace('.tamildbox.tips', '.tamilgun.tv')" in html1:
#             url = url.replace('hls_vast', 'hls')
#             url = url.replace('.tamildbox.tips', '.tamilgun.tv')
#             url = url + '/playlist.m3u8'
#             #xbmc.log(url)
#             return url
#     return None

def getcontent(url):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    return html

def getcontenttamildbox(url):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'DNT': '1',
        'Accept': '*/*',
        'Origin': 'https://embed1.tamildbox.tips',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://embed1.tamildbox.tips/',
        'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    }
    response = requests.get(url, headers=headers)
    return response


def resolve_embedtamilgun(url):
    if "embed1.tamildbox" in url:
        #xbmc.log("---------------------------------------embed1-tamildbox-----------------------------------------------------------")
##        if "https" in url:
##            url = url.replace("https","http")
##        elif "http" in url:
##            url = url
##        else:
##            url = 'http:'+url
        html = getcontent(url)
        movieurl= re.compile("domainStream = '(.*?)'").findall(html)
        if movieurl:
            for tempurl in movieurl:
                if tempurl:
                    print(tempurl)
                    movieurlx = tempurl.replace("hls","hls1mp4/2020")
                    temp = getcontenttamildbox(movieurlx)
                    id = re.compile("nimblesessionid=(.*?)&").findall(temp.text)
                    nimble = "chunk.m3u8?nimblesessionid="
                    nimbleid = nimble+id[0]
                    movieurlx = movieurlx.replace("playlist.m3u8",nimbleid)
                    return movieurlx
        elif "domainStream = domainStream.replace('.tamildbox.tips', '.tamilgun.tv')" in html1:
            url = url.replace('hls_vast', 'hls')
            url = url.replace('.tamildbox.tips', '.tamilgun.tv')
            url = url + '/playlist.m3u8'

            return url
    return None