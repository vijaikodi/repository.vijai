#https://github.com/tamland/kodi-plugin-routing
import routing
import xbmcgui
from xbmcgui import ListItem, Dialog
from xbmcplugin import addDirectoryItem, endOfDirectory, setResolvedUrl
import urllib.request, urllib.error, urllib.parse,urllib.request,urllib.parse,urllib.error,re,requests
import resolveurl as urlresolver
from lib import chromevideo, embedtamilgun, vidorgnet, videobin, vup, gofile, streamtape
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
def getredirectedurl(url):
	try:
		r= requests.get(url,verify=False)
		return r.url
	except Exception as e:
		Dialog().ok('XBMC', str(e))
def loadmainlist(url,title,get_site_content_regex,get_stream_url_regex,get_nav_data_regex):
    url = getredirectedurl(url)
    get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
    get_stream_url_regex = urllib.parse.quote_plus(get_stream_url_regex)
    get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
    addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem(title), True)


plugin = routing.Plugin()
@plugin.route('/')
def index():
    response = requests.get("https://raw.githubusercontent.com/vijaikodi/repository.vijai/master/json")
    responsetext = response.text
    responsetext = responsetext.replace('\n', '')
    try:
        mainlist = json.loads(response.text)
    except:
        Dialog().ok('XBMC', 'Error in Json Loading')
    if mainlist:
        for p in mainlist:
            #loadmainlist(p['url'],p['title'],p['get_site_content_regex'],p['get_stream_url_regex'],p['get_nav_data_regex'])
            url = getredirectedurl(p['url'])
            url = urllib.parse.quote_plus(url)
            get_site_content_regex = urllib.parse.quote_plus(p['get_site_content_regex'])
            get_stream_url_regex = urllib.parse.quote_plus(p['get_stream_url_regex'])
            get_nav_data_regex = urllib.parse.quote_plus(p['get_nav_data_regex'])
            title = p['title']
            try:
                addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem(title), True)
            except:
                Dialog().ok(title, 'Unable to load this site')

    # print (p['title'])
    # # addDirectoryItem(plugin.handle, plugin.url_for(show_category,"https://6movierulz.com/category/tamil-movie/"), ListItem("Category One"), True)
    # # addDirectoryItem(plugin.handle, plugin.url_for(show_category, "two"), ListItem("Category Two"), True)
    # # addDirectoryItem(plugin.handle, plugin.url_for(show_directory, "/dir/two"), ListItem("Directory Two"), True)
    # movierulzurl = getredirectedurl("http://4movierulz.com")
    # # r = requests.get(url,verify=False) 
    # # movierulzurl = r.url
    # if movierulzurl:
	   #  url = movierulzurl+"/category/tamil-movie/"
	   #  get_site_content_regex ='<a href=\"(?P<pageurl>.*?)\"\stitle=\"(?P<title>.*?)\">\s*<img width=\"\d+\" height=\"\d+\" src=\"(?P<poster>.*?)\"'
	   #  get_stream_url_regex = '<p><strong>(?P<streamtitle>.*?)<\/strong><br \/>\s+<a href=\"(?P<streamurl>.*?)\"'
	   #  get_nav_data_regex = '<a href=\"(?P<navlink>.*?)\">&larr;(\s|)Older Entries'
	   #  get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
	   #  get_stream_url_regex = urllib.parse.quote_plus(get_stream_url_regex)
	   #  get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
	   #  addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem("movierulz-Tamil"), True)
	   #  url = movierulzurl+"/bollywood-movie-free/"
	   #  addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem("movierulz-Hindi"), True)
	   #  url = movierulzurl+"/category/telugu-movies-2020/"
	   #  addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem("movierulz-Telugu"), True)
    # url = "https://www.tubetamil.com"
    # get_site_content_regex='<div class="thumb">\s+<a\shref=\"(?P<pageurl>.*?)\"\s+title=\"(?P<title>.*?)\">\s+<img\ssrc=\"(?P<poster>.*?)\"'
    # get_nav_data_regex = '<li class="next"><a\shref=\"(?P<navlink>.*?)\"'
    # get_stream_url_regex = '<iframe\swidth=\"(.*?)\"\s+height=\"(.*?)\"\s+src=\"(?P<streamurl>.*?)\?'
    # get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
    # get_stream_url_regex = urllib.parse.quote_plus(get_stream_url_regex)
    # get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
    # addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem("Tubetamil"), True)
    # url= getredirectedurl("http://tamilgun.com")
    # if url:
	   #  tamilgunurl = url.replace('/tamil/','')
	   #  url = tamilgunurl +'/categories/new-movies-a/'
	   #  get_site_content_regex = '<img src=\" (?P<poster>.*?) \" alt=\"(?P<title>.*?)\" \/>\s+<div class=\"rocky-effect\">\s+<a href=\"(?P<pageurl>.*?)\"\s>'
	   #  get_nav_data_regex = '<a class="next page-numbers" href="(?P<navlink>.*?)">'
	   #  get_stream_url_regex = '<(iframe|IFRAME)(\s|.*?)(src|SRC)=\"(?P<streamurl>.*?)\"|onclick=\"window\.open\(\'(?P<streamurl1>.*?)\'|sources:\s+\[{\"file\":\"(?P<streamurl2>.*?)\"}\]'
	   #  get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
	   #  get_stream_url_regex = urllib.parse.quote_plus(get_stream_url_regex)
	   #  get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
	   #  addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem("Tamilgun-NewMovies"), True)
	   #  url = tamilgunurl +'/categories/hd-movies/'
	   #  get_site_content_regex = '<img src=\" (?P<poster>.*?) \" alt=\"(?P<title>.*?)\" \/>\s+<div class=\"rocky-effect\">\s+<a href=\"(?P<pageurl>.*?)\"\s>'
	   #  get_nav_data_regex = '<a class="next page-numbers" href="(?P<navlink>.*?)">'
	   #  get_stream_url_regex = '<(iframe|IFRAME)(\s|.*?)(src|SRC)=\"(?P<streamurl>.*?)\"|onclick=\"window\.open\(\'(?P<streamurl1>.*?)\'|sources:\s+\[{\"file\":\"(?P<streamurl2>.*?)\"}\]'
	   #  get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
	   #  get_stream_url_regex = urllib.parse.quote_plus(get_stream_url_regex)
	   #  get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
	   #  addDirectoryItem(plugin.handle, plugin.url_for(getsitecontent,url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex), ListItem("Tamilgun-HDMovies"), True)
    endOfDirectory(plugin.handle)


@plugin.route('/getsitecontent/<path:url>/<get_site_content_regex>/<get_nav_data_regex>/<get_stream_url_regex>')
def getsitecontent(url,get_site_content_regex,get_nav_data_regex,get_stream_url_regex):
    url = urllib.parse.unquote_plus(url)
    get_site_content_regex = urllib.parse.unquote_plus(get_site_content_regex)
    get_nav_data_regex = urllib.parse.unquote_plus(get_nav_data_regex)
    data = getdatacontent_dict(url,get_site_content_regex)
    nav = getdatacontent_dict(url,get_nav_data_regex)
    for item in data:
        listitem = xbmcgui.ListItem(item['title'])
        #ListItem.setLabel(item['title'])
        listitem.setArt({ 'poster': item['poster'], 'thumb' : item['poster']})
        #addDirectoryItem(plugin.handle,plugin.url_for(liststreamurl,item['pageurl'],get_stream_url_regex), ListItem(label=item['title'],icon=item['poster']),True)
        addDirectoryItem(plugin.handle,plugin.url_for(liststreamurl,item['pageurl'],get_stream_url_regex), listitem,True)
        xbmc.log(item['poster'])
        xbmc.log(item['title'])
    if nav:
        get_site_content_regex = urllib.parse.quote_plus(get_site_content_regex)
        get_nav_data_regex = urllib.parse.quote_plus(get_nav_data_regex)
        nav = nav[0]
        if nav['navlink']:
            nav = nav['navlink']
            addDirectoryItem(plugin.handle,plugin.url_for(getsitecontent,nav,get_site_content_regex,get_nav_data_regex,get_stream_url_regex),ListItem("[B]Next Page...[/B]"),True)
    endOfDirectory(plugin.handle)

@plugin.route('/liststreamurl/<path:url>/<get_stream_url_regex>')
def liststreamurl(url,get_stream_url_regex):
    get_stream_url_regex = urllib.parse.unquote_plus(get_stream_url_regex)
    data = getdatacontent_dict(url,get_stream_url_regex)
    blacklists = ['goblogportal']
    for item in data:
        xbmc.log(str(item))
        for key, value in list(item.items()):

            if 'streamurl'in key:
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
    endOfDirectory(plugin.handle)

@plugin.route('/resolvelink/<path:url>/<source>')
#source variable is used for resolving custom resolver coming from source site ex: videobin.co from movierulz can be routed particular if loop, the rest will be resolved by urlresolver
def resolvelink(url,source):
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
    elif 'chrome.video' in url:
        movieurl = resolve_chromevideo(url)
        try:
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
    elif 'vidorg' in url:
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
    elif 'vup' in url and 'movierulz' in source:
        movieurl = vup.resolve_vup(url)
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
        movieurl = streamtape.resolve_streamtape(url)
        try:
            addDirectoryItem(plugin.handle,url=movieurl,listitem=play_item,isFolder=False)
        except:
            Dialog().ok('XBMC', 'Unable to locate video')
    elif 'etcsrs' in url and 'movierulz' in source:
        #mixdrop link
        reg ='class="main-button dlbutton" href="(.*?)"'
        url = getdatacontent(url,reg)
        url = url[0]
        try:
            movieurl = urlresolver.HostedMediaFile(url)
            movieurl = movieurl.resolve()
            xbmc.log(movieurl)
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


if __name__ == '__main__':
    plugin.run()