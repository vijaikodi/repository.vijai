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
    return data
def getredirectedurl(url):
    try:
        r= requests.get(url,verify=False)
        return r.url
    except Exception as e:
        Dialog().ok('XBMC', str(e))

def resolve_arivakam(url,source):
    #web_pdb.set_trace()
    ##Player3.arivakam.net
    id = url.split('/')
    id = id [-1]
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': url,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

    params = {
        'id': id,
    }

    response = requests.get('https://player3.arivakam.net/api/movie', params=params, headers=headers)
    data = response.text
    reg = '\"urlStream\":\"(.*?)\"'
    data = re.compile(reg).findall(data)
    if data:
        streamurl = data[0]
        return streamurl
    else:
        return None

    
    ## Player2.arivakam.com
    # id = url.split('=')
    # id = id [-1]
    # headers = {
    # 'authority': 'player2.arivakam.net',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    # 'dnt': '1',
    # 'referer': source,
    # 'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'iframe',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'cross-site',
    # 'upgrade-insecure-requests': '1',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    # }

    # params = {
    #     'id': id,
    # }

    # response = requests.get('https://player2.arivakam.net/player/', params=params, headers=headers)

    # reg = '\"file\":\"(.*?)\"'
    # html = response.text
    # data = re.compile(reg).findall(html)
    # if data:
    #     streamurl = data[0]
    #     return streamurl
    # else:
    #     return None







# def resolve_arivakam(url):
#     try:
#         reg = '"file":\"(.*?)\"'
#         link1 = getdatacontent(url,reg)
#         link1 = link1[0]
#         link = getredirectedurl(link1)
#         link = link.split("?")
#         link = link[0]
#         t1 = urlparse(link)
#         t2 = t1.path
#         r = t1.path.split("/")[-2].split(",")[-1]
#         t3 = t2.split("/")
#         t3[-2] = r
#         r = "/".join(t3)
#         t=t1._replace(path=r)
#         link = t.geturl()
#         #xbmc.log("----------------------------------------Arivakam----------------------------------------------------------------")
#         #xbmc.log(link)
#         #['https://32vod-adaptive.akamaized.net/exp=1631566344~acl=%2Fd5994a51-6d0f-410c-8cab-f0e2b55704af%2F%2A~hmac=9ba5e07383d402bd8f10f4692eae6f169647905e44541f7e1f4d5b3d6aa9c5f6/d5994a51-6d0f-410c-8cab-f0e2b55704af/sep/video/589c9043,281f15ba,279905cd,43a500be/master.m3u8', 'absolute=1']
#         return link
#     except:
#         return None    









# def resolve_arivakam(url):
#     try:
#         headers = {
#         'authority': 'play.arivakam.net',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-language': 'en-US,en;q=0.9',
#         'referer': 'https://tamilgun.asia/',
#         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'iframe',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'cross-site',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
#         }
#         response = requests.get(url, headers=headers, verify=False)
#         reg = '"file":\"(.*?)\"'
#         data = re.compile(reg).findall(response.text)
#         xbmc.log('--------------------------------------Entering Arivakam DATA Key = 1-----------------------------------------------------')
#         xbmc.log(str(data))
#         for url in data:
#             if 'vimeo' in url:
#                 #xbmc.log(url)
#                 headers = {
#                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#                     'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
#                     'Connection': 'keep-alive',
#                     'DNT': '1',
#                     'Referer': 'https://play.arivakam.net/',
#                     'Sec-Fetch-Dest': 'iframe',
#                     'Sec-Fetch-Mode': 'navigate',
#                     'Sec-Fetch-Site': 'cross-site',
#                     'Upgrade-Insecure-Requests': '1',
#                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#                     'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
#                     'sec-ch-ua-mobile': '?0',
#                     'sec-ch-ua-platform': '"Windows"',
#                 }
#                 #response = requests.get(url, headers=headers)
#                 reg = "\"avc_url\":\"(.*?)\""
#                 tempurl = getdatacontent(url,reg)
#                 #url = re.compile(reg).findall(response)
#                 xbmc.log('------------------------------------------ENtering Arivakam------------------------------------------------------------------')
#                 ##xbmc.log(str(response))
#                 xbmc.log(str(tempurl))
#                 if tempurl:
#                     url = tempurl[2]
#                     return url
#                 else:
#                     xbmc.log('------------------------------------------ENtering Arivakam 2 ------------------------------------------------------------------')
#                     try:
#                         return url
#                     except:
#                         Dialog().ok('XBMC', 'Unable to locate video')
#                     return None
#             if 'cdntest.diebutx' in url:
#                 if url:
#                     t = url.split('playlist.m3u8')
#                     start_url = t[0]
#                     xbmc.log(start_url)
#                     reg = "NAME=720p\s+(.*?)\s+#EXT"
#                     end_url = getdatacontent(url,reg)
#                     if end_url:
#                         end_url = end_url[0]
#                         xbmc.log(end_url)
#                         url = start_url+end_url
#                         xbmc.log(url)
#                         return url
#                     else:
#                         return None
#                 else:
#                     return None
#             else:
#                 return None
#     except:
#         Dialog().ok('XBMC', 'Unable to locate video')

#-----------------------------------------------------------------------------------------------------------------------------
    # url = url.split('=')
    # url = url[1]
    # url = url.rstrip(url[-1])
    # turl ='https://play.arivakam.net/player/api_player.php?id='+url+'&type=hls&key=1'
    # #xbmc.log('--------------------------------------Entering Arivakam-----------------------------------------------------')
    # #xbmc.log(turl)
    # reg = 'eval(.*?)\s+<'
    # resp = getdatacontent(turl,reg)
    # if resp:
    #     data = unpack(resp[0])
    #     reg = '"file":\"(.*?)\"'
    #     data = re.compile(reg).findall(data)
    #     #xbmc.log('--------------------------------------Entering Arivakam DATA Key = 1-----------------------------------------------------')
    #     #xbmc.log(str(data))
    #     url = data[0]
    #     if 'vimeo' in url:
    #         #xbmc.log(url)
    #         headers = {
    #         'Accept': '*/*',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #         'Connection': 'keep-alive',
    #         'Origin': 'https://play.arivakam.net',
    #         'Referer': 'https://play.arivakam.net/',
    #         'Sec-Fetch-Dest': 'empty',
    #         'Sec-Fetch-Mode': 'cors',
    #         'Sec-Fetch-Site': 'cross-site',
    #         'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36',
    #         'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    #         'sec-ch-ua-mobile': '?1',
    #         'sec-ch-ua-platform': '"Android"',
    #         }
    #         response = requests.get(url, headers=headers,allow_redirects=False)
    #         url = response.headers['Location']
    #         #xbmc.log('------------------------------------------ENtering Arivakam------------------------------------------------------------------')
    #         #xbmc.log(url)
    #         if url:
    #             return url
    #         else:
    #             return None
    #     elif 'playallu' in url:
    #         #xbmc.log('------------------------------------------ENtering Playallu------------------------------------------------------------------')
    #         #xbmc.log(url)
    #         movieurl = playallu.resolve_playallu(url)
    #         if movieurl:
    #             return url
    #         else:
    #             return None
    # else:
    #     turl ='https://play.arivakam.net/player/api_player.php?id='+url+'&type=hls&key=0'
    #     #xbmc.log('--------------------------------------Entering Arivakam DATA Key = 0-----------------------------------------------------')
    #     #xbmc.log(turl)
    #     reg = 'eval(.*?)\s+<'
    #     resp = getdatacontent(turl,reg)
    #     if resp:
    #         data = unpack(resp[0])
    #         reg = '"file":\"(.*?)\"'
    #         data = re.compile(reg).findall(data)
    #         url = data[0]
    #         if 'vimeo' in url:
    #             #xbmc.log(url)
    #             headers = {
    #             'Accept': '*/*',
    #             'Accept-Language': 'en-US,en;q=0.9',
    #             'Connection': 'keep-alive',
    #             'Origin': 'https://play.arivakam.net',
    #             'Referer': 'https://play.arivakam.net/',
    #             'Sec-Fetch-Dest': 'empty',
    #             'Sec-Fetch-Mode': 'cors',
    #             'Sec-Fetch-Site': 'cross-site',
    #             'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36',
    #             'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    #             'sec-ch-ua-mobile': '?1',
    #             'sec-ch-ua-platform': '"Android"',
    #             }
    #             response = requests.get(url, headers=headers,allow_redirects=False)
    #             url = response.headers['Location']
    #             #xbmc.log('------------------------------------------ENtering Arivakam------------------------------------------------------------------')
    #             #xbmc.log(url)
    #             if url:
    #                 return url
    #             else:
    #                 return None
    #         elif 'playallu' in url:
    #             #xbmc.log('------------------------------------------ENtering Playallu------------------------------------------------------------------')
    #             #xbmc.log(url)
    #             movieurl = playallu.resolve_playallu(url)
    #             if movieurl:
    #                 return url
    #             else:
    #                 return None


    # try:
    #         turl ='https://play.arivakam.net/player/api_player.php?id='+url+'&type=hls&key=1'
    #         #xbmc.log('--------------------------------------Entering Arivakam-----------------------------------------------------')
    #         #xbmc.log(turl)
    #         reg = 'eval(.*?)\s+<'
    #         resp = getdatacontent(turl,reg)
    #         data = unpack(resp[0])
    #         reg = '"file":\"(.*?)\"'
    #         data = re.compile(reg).findall(data)
    #         if data[0]:
    #             #xbmc.log('--------------------------------------Entering Arivakam DATA Key = 1-----------------------------------------------------')
    #             #xbmc.log(str(data))
    #             url = data[0]
    #             if 'vimeo' in url:
    #                 #xbmc.log(url)
    #                 headers = {
    #                 'Accept': '*/*',
    #                 'Accept-Language': 'en-US,en;q=0.9',
    #                 'Connection': 'keep-alive',
    #                 'Origin': 'https://play.arivakam.net',
    #                 'Referer': 'https://play.arivakam.net/',
    #                 'Sec-Fetch-Dest': 'empty',
    #                 'Sec-Fetch-Mode': 'cors',
    #                 'Sec-Fetch-Site': 'cross-site',
    #                 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36',
    #                 'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    #                 'sec-ch-ua-mobile': '?1',
    #                 'sec-ch-ua-platform': '"Android"',
    #                 }
    #                 response = requests.get(url, headers=headers,allow_redirects=False)
    #                 url = response.headers['Location']
    #                 #xbmc.log('------------------------------------------ENtering Arivakam------------------------------------------------------------------')
    #                 #xbmc.log(url)
    #                 if url:
    #                     return url
    #                 else:
    #                     return None
    #             elif 'playallu' in url:
    #                 #xbmc.log('------------------------------------------ENtering Playallu------------------------------------------------------------------')
    #                 #xbmc.log(url)
    #                 movieurl = playallu.resolve_playallu(url)
    #                 if movieurl:
    #                     return url
    #                 else:
    #                     return None
    #         else:
    #             turl ='https://play.arivakam.net/player/api_player.php?id='+url+'&type=hls&key=0'
    #             #xbmc.log('--------------------------------------Entering Arivakam DATA Key = 0-----------------------------------------------------')
    #             #xbmc.log(turl)
    #             reg = 'eval(.*?)\s+<'
    #             resp = getdatacontent(turl,reg)
    #             data = unpack(resp[0])
    #             reg = '"file":\"(.*?)\"'
    #             data = re.compile(reg).findall(data)
    #             if data[0]:
    #                 url = data[0]
    #                 if 'vimeo' in url:
    #                     #xbmc.log(url)
    #                     headers = {
    #                     'Accept': '*/*',
    #                     'Accept-Language': 'en-US,en;q=0.9',
    #                     'Connection': 'keep-alive',
    #                     'Origin': 'https://play.arivakam.net',
    #                     'Referer': 'https://play.arivakam.net/',
    #                     'Sec-Fetch-Dest': 'empty',
    #                     'Sec-Fetch-Mode': 'cors',
    #                     'Sec-Fetch-Site': 'cross-site',
    #                     'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36',
    #                     'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    #                     'sec-ch-ua-mobile': '?1',
    #                     'sec-ch-ua-platform': '"Android"',
    #                     }
    #                     response = requests.get(url, headers=headers,allow_redirects=False)
    #                     url = response.headers['Location']
    #                     #xbmc.log('------------------------------------------ENtering Arivakam------------------------------------------------------------------')
    #                     #xbmc.log(url)
    #                     if url:
    #                         return url
    #                     else:
    #                         return None
    #                 elif 'playallu' in url:
    #                     #xbmc.log('------------------------------------------ENtering Playallu------------------------------------------------------------------')
    #                     #xbmc.log(url)
    #                     movieurl = playallu.resolve_playallu(url)
    #                     if movieurl:
    #                         return url
    #                     else:
    #                         return None

    #     except:
    #         Dialog().ok('XBMC', 'Unable to locate video')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # else:
    #     reg = '<iframe id="embedvideo" src=\"(.*?)\"'
    #     resp = getdatacontent(url,reg)
    #     if resp:
    #         link = resp[0]
    #         movieurl = playallu.resolve_playallu(link)
    #         link = movieurl
    # return link
