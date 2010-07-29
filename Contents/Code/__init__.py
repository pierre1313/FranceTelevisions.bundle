# PMS plugin framework
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *
import re

####################################################################################################

PLUGIN_PREFIX           = "/video/francetelevisions"
PLUGIN_ID               = "com.plexapp.plugins.francetelevisions"
PLUGIN_REVISION         = 0.2
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
    dir.Append(Function(DirectoryItem(ChannelSubMenu,"Par chaîne")))
    dir.Append(Function(DirectoryItem(GenreSubMenu,"Par genre")))
    dir.Append(Function(DirectoryItem(RegionSubMenu,"Par région")))
    return dir

def ChannelSubMenu (sender):
    dir = MediaContainer(title2="Chaînes", viewGroup="Showcase", noCache=True)

    dir.Append(Function(DirectoryItem(RSS_parser,"France2",thumb="http://www.francetelevisions.fr/images/france2_logo.gif"),pageurl = "http://www.pluzz.fr/france2/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France3",thumb="http://www.francetelevisions.fr/images/france3_logo.gif"),pageurl = "http://www.pluzz.fr/france3/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France4",thumb="http://www.francetelevisions.fr/images/france4_logo.gif"),pageurl = "http://www.pluzz.fr/france4/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France5",thumb="http://www.francetelevisions.fr/images/france5_logo.gif"),pageurl = "http://www.pluzz.fr/france5/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"FranceO",thumb="http://www.francetelevisions.fr/images/franceO_logo.gif"),pageurl = "http://www.pluzz.fr/franceo/rss" ))
    return dir

def GenreSubMenu (sender):
    dir = MediaContainer(title2="Genre", viewGroup="List", noCache=True)

    dir.Append(Function(DirectoryItem(RSS_parser,"JT"),pageurl = "http://www.pluzz.fr/jt/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Découverte"),pageurl = "http://www.pluzz.fr/decouverte/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Séries - Fictions"),pageurl = "http://www.pluzz.fr/series---fictions/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Vie Pratique"),pageurl = "http://www.pluzz.fr/vie-pratique/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Culture"),pageurl = "http://www.pluzz.fr/culture/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Actu - Societé"),pageurl = "http://www.pluzz.fr/actu---societe/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Ludo"),pageurl = "http://www.pluzz.fr/ludo/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Divertissements"),pageurl = "http://www.pluzz.fr/divertissement/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Sports"),pageurl = "http://www.pluzz.fr/sports/rss" ))
    return dir

def RegionSubMenu (sender):
    dir = MediaContainer(title2="Regions", viewGroup="List", noCache=True)

    dir.Append(Function(DirectoryItem(RSS_parser,"Alsace"),pageurl = "http://www.pluzz.fr/alsace/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Aquitaine"),pageurl = "http://www.pluzz.fr/aquitaine/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Bourgogne"),pageurl = "http://www.pluzz.fr/bourgogne/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Franche-Comté"),pageurl = "http://www.pluzz.fr/franche-comte/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Corse"),pageurl = "http://www.pluzz.fr/corse/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Limousin"),pageurl = "http://www.pluzz.fr/limousin/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Poitou-Charentes"),pageurl = "http://www.pluzz.fr/poitou-charentes/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Lorraine"),pageurl = "http://www.pluzz.fr/lorraine/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Champagne-Ardenne"),pageurl = "http://www.pluzz.fr/champ[agne-ardenne/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Provence-Alpes"),pageurl = "http://www.pluzz.fr/provence-alpes/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Côte d'Azur"),pageurl = "http://www.pluzz.fr/cote-d-azur/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Nord-Pas-de-Calais"),pageurl = "http://www.pluzz.fr/nord-pas-de-calais/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Picardie"),pageurl = "http://www.pluzz.fr/picardie/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Haute-Normandie"),pageurl = "http://www.pluzz.fr/haute-normandie/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Basse-Normandie"),pageurl = "http://www.pluzz.fr/basse-normandie/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Bretagne"),pageurl = "http://www.pluzz.fr/bretagne/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Pays de la Loire"),pageurl = "http://www.pluzz.fr/pays-de-la-loire/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Paris Ile-de-France"),pageurl = "http://www.pluzz.fr/paris-ile-de-france/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Centre"),pageurl = "http://www.pluzz.fr/centre/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Rhône-Alpes"),pageurl = "http://www.pluzz.fr/rhone-alpes/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Auvergne"),pageurl = "http://www.pluzz.fr/auvergne/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Alpes"),pageurl = "http://www.pluzz.fr/alpes/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Midi-Pyrénées"),pageurl = "http://www.pluzz.fr/midi-pyrenees/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Languedoc-Roussillon"),pageurl = "http://www.pluzz.fr/langedoc-rousillon/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Réunion"),pageurl = "http://www.pluzz.fr/reunion/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Guyane"),pageurl = "http://www.pluzz.fr/guyane/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Polynésie"),pageurl = "http://www.pluzz.fr/polynesie/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Martinique"),pageurl = "http://www.pluzz.fr/martinique/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Mayotte"),pageurl = "http://www.pluzz.fr/mayotte/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Nouvelle Calédonie"),pageurl = "http://www.pluzz.fr/nouvelle-caledonie/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Guadeloupe"),pageurl = "http://www.pluzz.fr/guadeloupe/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Wallis et Futuna"),pageurl = "http://www.pluzz.fr/wallis-et-futuna/rss" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Saint-Pierre et Miquelon"),pageurl = "http://www.pluzz.fr/saint-pierre-et-miquelon/rss" ))

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

      
