Ôªø# PMS plugin framework
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *
import re

####################################################################################################

PLUGIN_PREFIX           = "/video/francetelevisions"
PLUGIN_ID               = "com.plexapp.plugins.francetelevisions"
PLUGIN_REVISION         = 0.4
PLUGIN_UPDATES_ENABLED  = True

PLAYER_PATH = "mms://a988.v101995.c10199.e.vm.akamaistream.net/7/988/10199/3f97c7e6/ftvigrp.download.akamai.com/10199/cappuccino/production/publication/"

NAME = L('France Televisions')

ART           = 'art-default.png'
ICON          = 'icon-default.png'

####################################################################################################

def Start():

    Plugin.AddPrefixHandler(PLUGIN_PREFIX, VideoMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)

def CreatePrefs():
    Prefs.Add(id='username', type='text', default='', label='Your Username')
    Prefs.Add(id='password', type='text', default='', label='Your Password', option='hidden')

def ValidatePrefs():
    u = Prefs.Get('username')
    p = Prefs.Get('password')
    ## do some checks and return a
    ## message container
    if( u and p ):
        return MessageContainer(
            "Success",
            "User and password provided ok"
        )
    else:
        return MessageContainer(
            "Error",
            "You need to provide both a user and password"
        )

def VideoMainMenu():

    dir = MediaContainer(viewGroup="List")

    dir.Append(Function(DirectoryItem(RSS_parser,"Tous les programmes"),pageurl = "http://www.pluzz.fr/rss" ))
    dir.Append(Function(DirectoryItem(ChannelSubMenu,"Par cha√Æne")))
    dir.Append(Function(DirectoryItem(GenreSubMenu,"Par genre")))
    dir.Append(Function(DirectoryItem(RegionSubMenu,"Par r√©gion")))
    
    return dir

def ChannelSubMenu (sender):
    dir = MediaContainer(title2="Cha√Ænes", viewGroup="Showcase", noCache=True)

    dir.Append(Function(DirectoryItem(RSS_parser,"France2",thumb="http://www.francetelevisions.fr/images/france2_logo.gif"),pageurl = "http://feeds.feedburner.com/Pluzz-France2?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France3",thumb="http://www.francetelevisions.fr/images/france3_logo.gif"),pageurl = "http://feeds.feedburner.com/Pluzz-France3?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France4",thumb="http://www.francetelevisions.fr/images/france4_logo.gif"),pageurl = "http://feeds.feedburner.com/Pluzz-France4?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France5",thumb="http://www.francetelevisions.fr/images/france5_logo.gif"),pageurl = "http://feeds.feedburner.com/Pluzz-France5?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"FranceO",thumb="http://www.francetelevisions.fr/images/franceO_logo.gif"),pageurl = "http://feeds.feedburner.com/Pluzz-FranceO?format=xml" ))

    return dir

def GenreSubMenu (sender):
    dir = MediaContainer(title2="Genre", viewGroup="List", noCache=True)

    dir.Append(Function(DirectoryItem(RSS_parser,"JT"),pageurl = "http://feeds.feedburner.com/Pluzz-Jt?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"D√©couverte"),pageurl = "http://feeds.feedburner.com/Pluzz-Decouverte?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"S√©ries - Fictions"),pageurl = "http://feeds.feedburner.com/Pluzz-Seriesfictions?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Vie Pratique"),pageurl = "http://feeds.feedburner.com/Pluzz-Viepratique?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Culture"),pageurl = "http://feeds.feedburner.com/Pluzz-Culture?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Actu - Societ√©"),pageurl = "http://feeds.feedburner.com/Pluzz-Actusociete?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Ludo"),pageurl = "http://feeds.feedburner.com/Pluzz-Ludo?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Divertissements"),pageurl = "http://feeds.feedburner.com/Pluzz-Divertissement?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Sports"),pageurl = "http://feeds.feedburner.com/Pluzz-Sports?format=xml" ))

    return dir

def RegionSubMenu (sender):
    dir = MediaContainer(title2="Regions", viewGroup="List", noCache=True)

    dir.Append(Function(DirectoryItem(RSS_parser,"Alsace"),pageurl = "http://feeds.feedburner.com/Pluzz-Alsace?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Aquitaine"),pageurl = "http://feeds.feedburner.com/Pluzz-Aquitaine?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Bourgogne"),pageurl = "http://feeds.feedburner.com/Pluzz-Bourgogne?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Franche-Comt√©"),pageurl = "http://feeds.feedburner.com/Pluzz-Franche-comte?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Corse"),pageurl = "http://feeds.feedburner.com/Pluzz-Corse?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Limousin"),pageurl = "http://feeds.feedburner.com/Pluzz-Limousin?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Poitou-Charentes"),pageurl = "http://feeds.feedburner.com/Pluzz-Poitou-charentes?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Lorraine"),pageurl = "http://feeds.feedburner.com/Pluzz-Lorraine?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Champagne-Ardenne"),pageurl = "http://feeds.feedburner.com/Pluzz-Champagne-ardenne?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Provence-Alpes"),pageurl = "http://feeds.feedburner.com/Pluzz-Provence-alpes?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"C√¥te d'Azur"),pageurl = "http://feeds.feedburner.com/Pluzz-Cote-d-azur?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Nord-Pas-de-Calais"),pageurl = "http://feeds.feedburner.com/Pluzz-Nord-pas-de-calais?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Picardie"),pageurl = "http://feeds.feedburner.com/Pluzz-Picardie?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Haute-Normandie"),pageurl = "http://feeds.feedburner.com/Pluzz-Haute-normandie?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Basse-Normandie"),pageurl = "http://feeds.feedburner.com/Pluzz-Basse-normandie?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Bretagne"),pageurl = "http://feeds.feedburner.com/Pluzz-Bretagne?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Pays de la Loire"),pageurl = "http://feeds.feedburner.com/Pluzz-Pays-de-la-loire?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Paris Ile-de-France"),pageurl = "http://feeds.feedburner.com/Pluzz-Paris-ile-de-france?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Centre"),pageurl = "http://feeds.feedburner.com/Pluzz-Centre?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Rh√¥ne-Alpes"),pageurl = "http://feeds.feedburner.com/Pluzz-Rhone-alpes?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Auvergne"),pageurl = "http://feeds.feedburner.com/Pluzz-Auvergne?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Alpes"),pageurl = "http://feeds.feedburner.com/Pluzz-Alpes?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Midi-Pyr√©n√©es"),pageurl = "http://feeds.feedburner.com/Pluzz-Midi-pyrenees?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Languedoc-Roussillon"),pageurl = "http://feeds.feedburner.com/Pluzz-Langedoc-rousillon?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"R√©union"),pageurl = "http://feeds.feedburner.com/Pluzz-Reunion?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Guyane"),pageurl = "http://feeds.feedburner.com/Pluzz-Guyane?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Polyn√©sie"),pageurl = "http://feeds.feedburner.com/Pluzz-Polynesie?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Martinique"),pageurl = "http://feeds.feedburner.com/Pluzz-Martinique?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Mayotte"),pageurl = "http://feeds.feedburner.com/Pluzz-Mayotte?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Nouvelle Cal√©donie"),pageurl = "http://feeds.feedburner.com/Pluzz-Nouvelle-caledonie?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Guadeloupe"),pageurl = "http://feeds.feedburner.com/Pluzz-Guadeloupe?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Wallis et Futuna"),pageurl = "http://feeds.feedburner.com/Pluzz-Wallis-et-futuna?format=xml" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Saint-Pierre et Miquelon"),pageurl = "http://feeds.feedburner.com/Pluzz-Saint-pierre-et-miquelon?format=xml" ))

    return dir

def get_stream (url):
    try:
      content = XML.ElementFromURL(url, isHTML='True', cacheTime=10).xpath("body/div/div/div/div/div/div[@id='playerCtnr']/a")
      for item in content:
        link = item.get("href")
        content = XML.ElementFromURL(link, isHTML='True', cacheTime=10).xpath("head/meta[@name='urls-url-video']")
        for item in content:
          videopath = item.get("content")
          if videopath != None:
            name = unicode(PLAYER_PATH + "/" + videopath,"utf-8")
          else:
            content = XML.ElementFromURL(link, isHTML='True', cacheTime=10).xpath("head/meta[@name='vignette-type-lien-externe-url']")
            for item in content:
              videopath = item.get("content")
              if videopath != None:
                name = unicode(videopath,"utf-8")
              else:
                return (None, None)
        
        content = XML.ElementFromURL(url, isHTML='True', cacheTime=10).xpath("head/meta[@name='programme_image']")
        for item in content:
          imagepath = item.get("content")
          if imagepath != None:
            vignette =  unicode("http://www.pluzz.fr" + imagepath,"utf-8")
          else:
            vignette = None
           
        return (name,vignette)
    except:
      return (None, None)


def RSS_parser(sender, pageurl , replaceParent=False,):
    tags = RSS.FeedFromURL(pageurl)
    dir = MediaContainer(title2=sender.itemTitle, viewGroup="List", replaceParent=replaceParent)

    for tag in tags["entries"]:
      (stream , vignette) = get_stream(tag["link"])
      if stream != None:
        dir.Append(WindowsMediaVideoItem(stream,width=384,height=216,title=tag["title"],summary='',thumb=vignette))
    return dir


     #     name = unicode(match_name.group(1),"utf-8")

   # html = HTTP.Request(url,encoding="Latin-1")
   # if html != None:
  #      name_pattern = re.compile('"(http://info.francetelevisions.fr[^"]+)"')
  #      match_name = name_pattern.search(html)
  #      name = ''
  #      if match_name != None:
  #        name = unicode(match_name.group(1),"utf-8")


          #html2 = HTTP.Request(name,encoding="Latin-1")
          #name_pattern = re.compile('urls-url-video" content="([^<>]+)"')
          #match_name = name_pattern.search(html2)
          #if match_name != None:
          #  name = unicode(PLAYER_PATH + "/" + match_name.group(1),"utf-8")
          #else :
          #    name_pattern = re.compile('vignette-type-lien-externe-url" content="([^<>]+)"')
          #    match_name = name_pattern.search(html2)
          #    if match_name != None:
          #      name = unicode(match_name.group(1),"utf-8")
              
          #name_pattern = re.compile('programme_image" content="([^<>]+)"')
          #match_name = name_pattern.search(html)
          #if match_name != None:
          #  vignette = unicode("http://www.pluzz.fr" + match_name.group(1),"utf-8")

      
