#https://github.com/tamland/kodi-plugin-routing
import routing
import web_pdb
import xbmcgui
import xbmcaddon
from xbmcgui import ListItem, Dialog
from xbmcplugin import addDirectoryItem, endOfDirectory, setResolvedUrl
import urllib.request, urllib.error, urllib.parse,urllib.request,urllib.parse,urllib.error,re,requests
import resolveurl as urlresolver
from lib import vidmx, chromevideo, embedtamilgun, vidorgnet, videobin, vupload, gofile, streamtape,etcscrs,arivakam, playallu, myfeminist, sendcm, downscrs,vembx, downlscr, downlsr, embedicu, watchlinkx, tamildhool, geodailymotion, vidplay, vcdnlare, directlinktx, filelinkzr,viralweb8, thrfiveio, mediadelivery
import json,os,xbmcvfs
from six.moves.html_parser import HTMLParser
import xbmc
import random
import base64
from resolveurl.lib import unjuice2

# To get help and inspect or debug the code use xbmc.log() or set_trace()
# xbmc.log(url)
# Place this line to trace the error
# web_pdb.set_trace()
def cleantitle(title):
    h = HTMLParser()
    cleanedtitle =h.unescape(title)
    return cleanedtitle

def getdatacontent_dict(url,reg):
    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(proxy_handler)
    req = urllib.request.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')]
    r = opener.open(req)
    html = r.read().decode('utf-8')
    r = re.compile(reg)
    data = [m.groupdict() for m in r.finditer(html)]
    return data


def getdatacontent_membednet_dict(url,reg):
    headers = {
    'authority': 'membed.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    r = re.compile(reg)
    data = [m.groupdict() for m in r.finditer(response.text)]
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

def getredirectedurl(url):
    try:
        url = urllib.parse.urlparse(url)
        url = url._replace(netloc=urllib.parse.urlparse((requests.get(url.scheme+'://'+url.netloc).url)).netloc)
        url = urllib.parse.urlunparse(url)
        return url
    except Exception as e:
        Dialog().ok('XBMC', str(e))

def is_absolute(url):
    return bool(urllib.parse.urlparse(url).netloc)
def is_scheme(url):
    parsed_url = urllib.parse.urlparse(url)
    return bool(parsed_url.scheme)

def jimkimble_redirectedurl(url):
    # Step 1: Parse the original URL
    original_url = url
    # Step 2: Extract JavaScript logic (domains and redirect logic)
    domains = ['https://www.jimkimble.com']
    # Randomly select a number between 1 and 4
    random_number = random.randint(1, 4)
    # Simulate the redirection based on the original JavaScript logic
    new_url = f"{domains[0]}/watch{random_number}.html"
    # Step 3: Append the original hash (URL fragment) to the new URL
    parsed_url = urllib.parse.urlparse(original_url)
    url_fragment = parsed_url.fragment  # Extract the fragment part (after the #)
    # Combine the new base URL with the fragment
    final_redirect_url = f"{new_url}#{url_fragment}"
    # Print the final redirected URL
    #print("Redirected URL:", final_redirect_url)
    return(final_redirect_url)

def loadmainlist(url,title,get_site_content_regex,get_stream_url_regex,get_nav_data_regex):
    #url = getredirectedurl(url)
    get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
    get_stream_url_regex = urllib.parse.quote_plus(get_stream_url_regex)
    get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
    addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem(title), True)

addon = xbmcaddon.Addon()
plugin = routing.Plugin()
@plugin.route('/')
def index():
    response = requests.get("https://raw.githubusercontent.com/vijaikodi/repository.vijai/master/resources/header.json")
    responsetext = response.text
    responsetext = responsetext.replace('\n', '')
    try:
        mainlist = json.loads(response.text)
    except:
        Dialog().ok('XBMC', 'Error in Json Loading')
    if mainlist:
        for p in mainlist:
            try:
                title = p['title']
                url = p['url']
                url = urllib.parse.quote_plus(url)
                addDirectoryItem(plugin.handle, plugin.url_for(listsites,url,title), ListItem(title), True)
            except:
                Dialog().ok(title, 'Unable to load this site')
    endOfDirectory(plugin.handle)

@plugin.route('/listsites/<path:url>/<title>')
def listsites(url,title):
    #web_pdb.set_trace()
    url = urllib.parse.unquote_plus(url)
    response = requests.get(url)
    responsetext = response.text
    responsetext = responsetext.replace('\n', '')
    try:
        mainlist = json.loads(response.text)
    except:
        Dialog().ok('XBMC', 'Error in Json Loading')
    if mainlist:
        for p in mainlist:
            if (addon.getSetting('adult') == 'true'):
                try:
                    #loadmainlist(p['url'],p['title'],p['get_site_content_regex'],p['get_stream_url_regex'],p['get_nav_data_regex'])
                    title = p['title']
                    url = p['url']
                    url = urllib.parse.quote_plus(url)
                    content_type = p['content_type']
                    get_site_content_regex = urllib.parse.quote_plus(p['get_site_content_regex'])
                    get_stream_url_regex = urllib.parse.quote_plus(p['get_stream_url_regex'])
                    get_nav_data_regex = urllib.parse.quote_plus(p['get_nav_data_regex'])
                    addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem(title), True)
                except:
                    Dialog().ok(title, 'Unable to load this site')
            elif (addon.getSetting('adult') == 'false'):
                try:
                    #loadmainlist(p['url'],p['title'],p['get_site_content_regex'],p['get_stream_url_regex'],p['get_nav_data_regex'])
                    title = p['title']
                    url = p['url']
                    url = urllib.parse.quote_plus(url)
                    content_type = p['content_type']
                    get_site_content_regex = urllib.parse.quote_plus(p['get_site_content_regex'])
                    get_stream_url_regex = urllib.parse.quote_plus(p['get_stream_url_regex'])
                    get_nav_data_regex = urllib.parse.quote_plus(p['get_nav_data_regex'])
                    if (content_type != "Mature-Content"):
                        addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem(title), True)
                except:
                    Dialog().ok(title, 'Unable to load this site')

    
    endOfDirectory(plugin.handle)


@plugin.route('/getsitecontent/<path:url>/<get_site_content_regex>/<get_nav_data_regex>/<get_stream_url_regex>')
def getsitecontent(url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex):
    url = urllib.parse.unquote_plus(url)
    url = getredirectedurl(url)
    get_site_content_regex = urllib.parse.unquote_plus(get_site_content_regex)
    get_nav_data_regex = urllib.parse.unquote_plus(get_nav_data_regex)
    data = getdatacontent_dict(url,get_site_content_regex)
    #web_pdb.set_trace()
    nav = getdatacontent_dict(url,get_nav_data_regex)
    for item in data:
        #web_pdb.set_trace()
        listitem = xbmcgui.ListItem(item['title'])
        #ListItem.setLabel(item['title'])
        if is_scheme(item['poster']):
            listitem.setArt({ 'poster': item['poster'], 'thumb' : item['poster']})
        else:
            base = urllib.parse.urlparse(item['poster'])
            base_new = base._replace(scheme='https')
            item['poster'] = urllib.parse.urlunparse(base_new)
            listitem.setArt({ 'poster': item['poster'], 'thumb' : item['poster']})
        #addDirectoryItem(plugin.handle,plugin.url_for(liststreamurl,item['pageurl'],get_stream_url_regex), ListItem(label=item['title'],icon=item['poster']),True)
        if 'synctogethr.com' in item['pageurl']:
            item['pageurl'] = jimkimble_redirectedurl(item['pageurl'])
            item['pageurl'] = urllib.parse.quote_plus(item['pageurl'])
        addDirectoryItem(plugin.handle,plugin.url_for(liststreamurl,item['pageurl'],get_stream_url_regex), listitem,True)
    if nav:
        #web_pdb.set_trace()
        get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
        get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
        nav = nav[0]
        if nav['navlink']:
            nav = nav['navlink']
            if is_absolute(nav):
                addDirectoryItem(plugin.handle,plugin.url_for(getsitecontent,nav,get_site_content_regex,get_nav_data_regex,get_stream_url_regex),ListItem("[B]Next Page...[/B]"),True)
            else:
                base = urllib.parse.urlparse(url)
                base_new = base._replace(path=nav)
                nav = urllib.parse.urlunparse(base_new)
                addDirectoryItem(plugin.handle,plugin.url_for(getsitecontent,nav,get_site_content_regex,get_nav_data_regex,get_stream_url_regex),ListItem("[B]Next Page...[/B]"),True)
    endOfDirectory(plugin.handle)


#Streamurl can be worked on this part of the code
#streamurl regex groupname ex: (?P<streamurl>.*?)   the streamurl can be captured in the key value of the dictionary and can be used for further logic
@plugin.route('/liststreamurl/<path:url>/<get_stream_url_regex>')
def liststreamurl(url,get_stream_url_regex):
    #web_pdb.set_trace()
    get_stream_url_regex = urllib.parse.unquote_plus(get_stream_url_regex)
    url = urllib.parse.unquote_plus(url)
    if 'jimkimble' in url:
        temp_url = urllib.parse.parse_qs(urllib.parse.urlparse(url).fragment).get('urls')
        urls = base64.b64decode(temp_url[0])
        urls = json.loads(urls.decode('utf-8'))
        if urls:
            for key,value in urls.items():
                title = key
                streamurl = urllib.parse.quote_plus(value)
                url = urllib.parse.quote_plus(url)
                addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,streamurl,url), ListItem(title),True)
        endOfDirectory(plugin.handle)
    else:
        try:
            data = getdatacontent_dict(url,get_stream_url_regex)
            blacklists = ['goblogportal']
            for item in data:
                if ('streamtitle'in item) and ('streamurl'in item):
                        #This loop helps list the titles of the stream provider ex; playarivalam, streamtape,vimeo etc
                        if item['streamurl']:
                            for blacklist in blacklists:
                                if blacklist in item['streamurl']:
                                    pass
                                else:
                                    streamurl = urllib.parse.quote_plus(item['streamurl'])
                                    title = urllib.parse.unquote_plus(item['streamtitle'])
                                    # Title needs to be cleaned but having an error with htmlparser module
                                    #title = cleantitle(title)
                                    url = urllib.parse.quote_plus(url)
                                    addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,streamurl,url), ListItem(title),True)
                else:
                    for key, value in list(item.items()):
                        #web_pdb.set_trace()
                        if "tamildhool_url" in key:
                            if ("insighthubnews" in value) or ("globalnewsphere" in value) or ("celebrityjest" in value):
                                reg = '<iframe.+?src="([^"]+)'
                                streamurl = urllib.parse.unquote_plus(value)
                                data = getdatacontent(streamurl,reg)
                                source = value
                                if data:
                                    streamurl = data[0]
                                    title = streamurl.split('/')
                                    title = title[2]+'-Link'
                                    streamurl = streamurl.replace('\n','')
                                    streamurl = urllib.parse.quote_plus(streamurl)
                                    source = urllib.parse.quote_plus(source)
                                    addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,streamurl,source), ListItem(title),True)
                            # if "globalnewsphere" in value:
                            #     #web_pdb.set_trace()
                            #     url = urllib.parse.unquote_plus(value)
                            #     reg ='iframe style=\"(.*?)\" frameborder=\"0\" type=\"(.*?)\" src=\"(?P<streamurl>(.|\n)*?)\"'
                            #     data = getdatacontent_dict(url,reg)
                            #     source = "tamildhool"
                            #     for item in data:
                            #         if 'thrfive.io' in item['streamurl']:
                            #             #web_pdb.set_trace()
                            #             url = item['streamurl']
                            #             url = url.replace('\n','')
                            #             headers = {
                            #                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            #                     'accept-language': 'en-US,en;q=0.9',
                            #                     #'priority': 'u=0, i',
                            #                     #'Connection': 'keep-alive',
                            #                     #'Host': 'thrfive.io',
                            #                     'referer': 'https://globalnewsphere.com/',
                            #                     #'sec-ch-ua': '"Google Chrome";v="128", "Chromium";v="125", "Not.A/Brand";v="24"',
                            #                     #'sec-ch-ua-mobile': '?0',
                            #                     # 'sec-ch-ua-platform': '"Windows"',
                            #                     # 'sec-fetch-dest': 'iframe',
                            #                     # 'sec-fetch-mode': 'navigate',
                            #                     # 'sec-fetch-site': 'cross-site',
                            #                     # 'upgrade-insecure-requests': '1',
                            #                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
                            #                 }
                            #             response = requests.get(url, headers=headers)
                            #             data = response.text
                            #             reg = '<script type="application\/javascript">(.*?)<\/script>'
                            #             code = re.compile(reg).findall(data)
                            #             temp = unjuice2.run(code[0]) 
                            #             reg = 'mpegURL\",\"file\":\"(.*?)\"'
                            #             url =  re.compile(reg).findall(temp)
                            #             url = url[0].replace("\\","")
                            #             play_item = ListItem('click to play the link')
                            #             play_item.setInfo( type="Video", infoLabels=None)
                            #             play_item.setProperty('IsPlayable', 'true')
                            #             addDirectoryItem(plugin.handle,url=url,listitem=play_item,isFolder=False)
                            #             #addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,url,source), ListItem('thrfive.io'),True)
                            #         if 'dailymotion' in item['streamurl']:
                            #             url = item['streamurl']
                            #             url = url.split('\n')
                            #             url = url[0]
                            #             addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,url,source), ListItem('dailymotion'),True)
                        if "hindilinks4u_streamurl" in key:
                            if 'membed.net'in value:
                                if value:
                                    url = urllib.parse.unquote_plus(value)
                                    reg = "<div class=\"dowload\"><a\s+href=\"(?P<streamurl>.*?)\"\starget=\'_blank\'>(?P<title>.*?)<\/a>"
                                    data = getdatacontent_membednet_dict(url,reg)
                                    source = "hindilinks4u"
                                    for item in data:
                                        if 'sbplay2' in item['streamurl']:
                                            url = item['streamurl']
                                            url = url.split('?')
                                            url = url[0]
                                            addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,url,source), ListItem(item['title']),True)
                                        if 'dood' in item['streamurl']:
                                            url = item['streamurl']
                                            url = url.split('?')
                                            url = url[0]
                                            addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,url,source), ListItem(item['title']),True)
                                        if 'embedsito' in item['streamurl']:
                                            url = item['streamurl']
                                            url = url.split('#')
                                            url = url[0]
                                            addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,url,source), ListItem(item['title']),True)
                                        if 'mixdrop' in item['streamurl']:
                                            url = item['streamurl']
                                            url = url.split('?')
                                            url = url[0]
                                            addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,url,source), ListItem(item['title']),True)
                        if 'streamurl'in key:
                            #This loop helps list the titles of the stream provider ex; playarivalam, streamtape,vimeo etc
                            if value:
                                for blacklist in blacklists:
                                    if blacklist in value:
                                        pass
                                    else:
                                        streamurl = urllib.parse.quote_plus(value)
                                        title = value.split('/')
                                        title = title[2]+'-Link'
                                        url = urllib.parse.quote_plus(url)
                                        addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,streamurl,url), ListItem(title),True)
                        if 'unescape'in key:
                            if value:
                                linkcode = urllib.parse.unquote_plus(value)
                                if "iframe src=" in linkcode:
                                    sources = re.findall('<iframe.+?src="([^"]+)', linkcode)
                                    for source in sources:
                                        streamurl = urllib.parse.quote_plus(source)
                                        title = source.split('/')
                                        title = title[2]+'-Link'
                                        url = urllib.parse.quote_plus(url)
                                        addDirectoryItem(plugin.handle,plugin.url_for(resolvelink,streamurl,url), ListItem(title),True)
            endOfDirectory(plugin.handle)
        except:
            endOfDirectory(plugin.handle)
            Dialog().ok('Loading site content', 'Unable to load this site')

@plugin.route('/resolvelink/<path:url>/<source>')
#source variable is used for resolving custom resolver coming from source site ex: videobin.co from movierulz can be routed particular if loop, the rest will be resolved by urlresolver
def resolvelink(url,source):
    #web_pdb.set_trace()
    url = urllib.parse.unquote_plus(url)
    source = urllib.parse.unquote_plus(source)
    play_item = ListItem('click to play the link')
    play_item.setInfo( type="Video", infoLabels=None)
    play_item.setProperty('IsPlayable', 'true')
    if 'youtube' in url:
        url = url.split('/')
        youtube_video_id = url[-1]
        url = 'plugin://plugin.video.youtube/play/?video_id='+youtube_video_id
        addDirectoryItem(plugin.handle,url=url,listitem=play_item,isFolder=False)
    # elif 'etcscrs' in url:
    #     data = getdatacontent_dict(url,'<iframe\swidth=\"(.*?)\"\sheight=\"(.*?)\"\s+src=\"(?P<mixdroplink>.*?)\"')
    #     for item in data:
    #         if item['mixdroplink']:
    #             if 'mixdrop' in item['mixdroplink']:
    #                 url = 'https:'+item['mixdroplink']
    #                 try:
    #                     movieurl = urlresolver.HostedMediaFile(url)
    #                     movieurl = movieurl.resolve()
    #                     addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
    #                 except:
    #                     Dialog().ok('XBMC', 'Unable to locate video')
    elif 'amtwkpbgjygpbp.pro' in url:
        try:
            addDirectoryItem(plugin.handle,url=url,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'chrome.video' in url:
        movieurl = chromevideo.resolve_chromevideo(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'arivakam' in url:
        #web_pdb.set_trace()
        if 'tamilgun' in source:
            url = url.replace('\/','/')
            url = url[:-1]
        movieurl = arivakam.resolve_arivakam(url,source)
        try:
            if type(movieurl) is list:
                for item in movieurl:
                    title = urllib.parse.urlparse(item).netloc
                    play_item = ListItem(title)
                    url = urllib.parse.unquote_plus(item)
                    addDirectoryItem(plugin.handle,url=url,listitem=play_item,isFolder=False)
            else:
                title = urllib.parse.urlparse(movieurl).netloc
                play_item = ListItem(title)
                url = movieurl
                addDirectoryItem(plugin.handle,url=url,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'viralweb8' in url:
        movieurl = viralweb8.resolve_viralweb8(url,source)
        try:
            for item in movieurl:
                title = 'click to play the link:'+item['quality']
                play_item = ListItem(title)
                url = item['url']
                addDirectoryItem(plugin.handle,url=url,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'vidplay' in url:
        movieurl = vidplay.resolve_vidplay(url,source)
        try:
            for item in movieurl:
                title = 'click to play the link:'+item[1]
                play_item = ListItem(title)
                url = item[0].replace("\"","")
                addDirectoryItem(plugin.handle,url=url,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'vcdnlare' in url:
        movieurl = vcdnlare.resolve_vcdnlare(url,source)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'myfeminist' in url:
        movieurl = myfeminist.resolve_myfeminist(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'downscrs' in url or 'downsrs' in url or 'downsscrs' in url or 'downssrs' in url:
        movieurl = downscrs.resolve_downscrs(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'downlscr' in url:
        movieurl = downlscr.resolve_downlscr(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'directlinktx' in url:
        #web_pdb.set_trace()
        movieurl = directlinktx.resolve_directlinktx(url,source)
        try:
            #setResolvedUrl(plugin.handle, True,listitem=play_item1)
            if movieurl[1] == 'Netutv':
                addDirectoryItem(plugin.handle,plugin.url_for(playlink,movieurl[0]),ListItem('click the link'),True)
            else:
                addDirectoryItem(plugin.handle,url=movieurl[0],listitem=play_item,isFolder=False) 
            #xbmc.Player().play(movieurl)
            #addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'filelinkzr' in url:
        #web_pdb.set_trace()
        movieurl = filelinkzr.resolve_filelinkzr(url,source)
        try:
            #setResolvedUrl(plugin.handle, True,listitem=play_item1)
            if movieurl[1] == 'Netutv':
                addDirectoryItem(plugin.handle,plugin.url_for(playlink,movieurl[0]),ListItem('click the link'),True)
            else:
                addDirectoryItem(plugin.handle,url=movieurl[0],listitem=play_item,isFolder=False) 
            #xbmc.Player().play(movieurl)
            #addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'downlsr' in url:
        movieurl = downlsr.resolve_downlsr(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'thrfive' in url:
        movieurl = thrfiveio.resolve_thrfiveio(url,source)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'mediadelivery' in url:
        movieurl = mediadelivery.resolve_mediadelivery(url,source)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'send.cm' in url:
        movieurl = sendcm.resolve_sendcm(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    
    elif 'playallu' in url:
        if 'tamilgun' in source:
            url = url.replace('\/','/')
        movieurl = playallu.resolve_playallu(url,source)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')

    elif 'vidmx' in url:
        movieurl = vidmx.resolve_vidmx(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'geo.dailymotion' in url:
        movieurl = geodailymotion.resolve_geodailymotion(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'vembx' in url:
        movieurl = vembx.resolve_vembx(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'embed.icu' in url:
        movieurl = embedicu.resolve_embedicu(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'watchlinkx' in url:
        movieurl = watchlinkx.resolve_watchlinkx(url)
        try:
            movieurl = urlresolver.HostedMediaFile(movieurl)
            movieurl = movieurl.resolve()
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif "embed1.tamildbox" in url:
        movieurl = embedtamilgun.resolve_embedtamilgun(url)
        try:
            if movieurl:
                addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
            else:
                Dialog().ok('XBMC', 'Unable to locate video')
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif "cdn.jwplayer" in url:
        movieurl = embedtamilgun.resolve_cdnjwplayer(url)
        try:
            if movieurl:
                addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
            else:
                Dialog().ok('XBMC', 'Unable to locate video')
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    # elif 'vimeo' in url and 'tamilgun' in source:
    #     movieurl = embedtamilgun.resolve_vimeo(url)
    #     try:
    #         addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
    #     except:
    #         Dialog().ok('XBMC', 'Unable to locate video')
    elif 'tamilray' in url and 'tamildhool' in source:
        movieurl = tamildhool.resolve_tamilray(url)
        try:
           addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
           Dialog().ok('XBMC', 'Unable to locate video')
    elif 'vidorg' in url and 'movierulz' in source:
        movieurl = vidorgnet.resolve_vidorgnet(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'videobin' in url and 'movierulz' in source:
        movieurl = videobin.resolve_videobin(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'vupload' in url and 'movierulz' in source:
        movieurl = vupload.resolve_vupload(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'gofile' in url and 'movierulz' in source:
        movieurl = gofile.resolve_gofile(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    # elif 'etcscrs' in url and 'movierulz' in source:
    #     #streamtape link
    #     reg = '<iframe src="(.*?)"'
    #     url = getdatacontent(url,reg)
    #     url = url[0]
    #     try:
    #         movieurl = urlresolver.HostedMediaFile(url)
    #         movieurl = movieurl.resolve()
    #         xbmc.log(movieurl)
    #         addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
    #     except:
    #         Dialog().ok('XBMC', 'Unable to locate video')
    elif 'etcscrs' in url and 'movierulz' in source:
        movieurl = etcscrs.resolve_etcscrs(url)
        if 'streamtape' in movieurl:
            movieurl = streamtape.resolve_streamtape(movieurl)
            try:
                addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
            except:
                Dialog().ok('XBMC', 'Unable to locate video')
        else:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'etcsrs' in url and 'movierulz' in source:
        #mixdrop link
        reg ='class="main-button dlbutton" href="(.*?)"'
        url = getdatacontent(url,reg)
        url = url[0]
        try:
            movieurl = urlresolver.HostedMediaFile(url)
            movieurl = movieurl.resolve()
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')

    else:
        try:
            movieurl = urlresolver.HostedMediaFile(url)
            movieurl = movieurl.resolve()
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    endOfDirectory(plugin.handle)

@plugin.route('/playlink/<path:url>')
#source variable is used for resolving custom resolver coming from source site ex: videobin.co from movierulz can be routed particular if loop, the rest will be resolved by urlresolver
def playlink(url):
    url = urllib.parse.unquote_plus(url)
    xbmc.Player().play(url)
    return False


if __name__ == '__main__':
    plugin.run()
    