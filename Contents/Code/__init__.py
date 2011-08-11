# -*- coding: utf-8 -*-
####################################################################################################
import re

PLUGIN_PREFIX           = "/video/francetelevisions"
PLUGIN_ID               = "com.plexapp.plugins.francetelevisions"
PLUGIN_REVISION         = 0.6
PLUGIN_UPDATES_ENABLED  = True

PLAYER_PATH = "mms://a988.v101995.c10199.e.vm.akamaistream.net/7/988/10199/3f97c7e6/ftvigrp.download.akamai.com/10199/cappuccino/production/publication/"
INFO_PATH = "http://www.pluzz.fr/appftv/webservices/video/getInfosVideo.php?src=capuccino&video-type=simple&template=ftvi&template-format=complet&id-externe="

NAME = L('France Televisions')

ART           = 'art-default.jpg'
ICON          = 'icon-default.png'

FEED_BASE_URL = "http://feeds.feedburner.com/Pluzz-%s?format=xml"
LOGO_URL = "http://www.francetelevisions.fr/images/france%s_logo.gif"

####################################################################################################  

import urllib2, httplib
class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_404(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_404(
            self, req, fp, code, msg, headers)
        Log(msg)
        return result

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(
            self, req, fp, code, msg, headers)
        result.status = code
        return result
        
    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(
            self, req, fp, code, msg, headers)
        result.status = code
        return result
        
###################################################################################################

def Start(): 

    Plugin.AddPrefixHandler(PLUGIN_PREFIX, VideoMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
    Plugin.AddViewGroup("Coverflow", viewMode="Coverflow", mediaType="items")

    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)
    
    HTTP.Headers["User-agent"] = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.19) Gecko/20110707 Firefox/3.6.19"


def VideoMainMenu():

    dir = MediaContainer(viewGroup="List")

    dir.Append(Function(DirectoryItem(RSS_parser,"Tous les programmes"),pageurl = "http://www.pluzz.fr/rss" ))
    dir.Append(Function(DirectoryItem(ChannelSubMenu,"Par chaîne")))
    dir.Append(Function(DirectoryItem(GenreSubMenu,"Par genre")))
    dir.Append(Function(DirectoryItem(RegionSubMenu,"Par région")))
    
    return dir

def ChannelSubMenu (sender):
    dir = MediaContainer(title2="Chaînes", viewGroup="Coverflow")

    dir.Append(Function(DirectoryItem(RSS_parser,"La 1ere",thumb=R('1ere-logo.png')),pageurl = FEED_BASE_URL % "La_1ere" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France2",thumb=R('France2-logo.png')),pageurl = FEED_BASE_URL % "France2" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France3",thumb=R('France3-logo.png')),pageurl = FEED_BASE_URL % "France3" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France4",thumb=R('France4-logo.png')),pageurl = FEED_BASE_URL % "France4" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France5",thumb=R('France5-logo.png')),pageurl = FEED_BASE_URL % "France5" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"FranceO",thumb=R('FranceO-logo.png')),pageurl = FEED_BASE_URL % "FranceO" ))

    return dir

def GenreSubMenu (sender):
    dir = MediaContainer(title2="Genre", viewGroup="List")

    dir.Append(Function(DirectoryItem(RSS_parser,"JT"),pageurl = FEED_BASE_URL % "Jt" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Découverte"),pageurl = FEED_BASE_URL % "Decouverte" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Séries - Fictions"),pageurl = FEED_BASE_URL % "Seriesfictions" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Vie Pratique"),pageurl = FEED_BASE_URL % "Viepratique" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Culture"),pageurl = FEED_BASE_URL % "Culture" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Actu - Societé"),pageurl = FEED_BASE_URL % "Actusociete" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Ludo"),pageurl = FEED_BASE_URL % "Ludo" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Divertissements"),pageurl = FEED_BASE_URL % "Divertissement" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Sports"),pageurl = FEED_BASE_URL % "Sports" ))

    return dir

def RegionSubMenu (sender):
    dir = MediaContainer(title2="Régions", viewGroup="List")

    dir.Append(Function(DirectoryItem(RSS_parser,"Alsace"),pageurl = FEED_BASE_URL % "Alsace" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Aquitaine"),pageurl = FEED_BASE_URL % "Aquitaine" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Bourgogne"),pageurl = FEED_BASE_URL % "Bourgogne" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Franche-Comté"),pageurl = FEED_BASE_URL % "Franche-comte" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Corse"),pageurl = FEED_BASE_URL % "Corse" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Limousin"),pageurl = FEED_BASE_URL % "Limousin" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Poitou-Charentes"),pageurl = FEED_BASE_URL % "Poitou-charentes" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Lorraine"),pageurl = FEED_BASE_URL % "Lorraine" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Champagne-Ardenne"),pageurl = FEED_BASE_URL % "Champagne-ardenne" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Provence-Alpes"),pageurl = FEED_BASE_URL % "Provence-alpes" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Côte d'Azur"),pageurl = FEED_BASE_URL % "Cote-d-azur" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Nord-Pas-de-Calais"),pageurl = FEED_BASE_URL % "Nord-pas-de-calais" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Picardie"),pageurl = FEED_BASE_URL % "Picardie" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Haute-Normandie"),pageurl = FEED_BASE_URL % "Haute-normandie" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Basse-Normandie"),pageurl = FEED_BASE_URL % "Basse-normandie" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Bretagne"),pageurl = FEED_BASE_URL % "Bretagne" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Pays de la Loire"),pageurl = FEED_BASE_URL % "Pays-de-la-loire" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Paris Ile-de-France"),pageurl = FEED_BASE_URL % "Paris-ile-de-france" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Centre"),pageurl = FEED_BASE_URL % "Centre" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Rhône-Alpes"),pageurl = FEED_BASE_URL % "Rhone-alpes" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Auvergne"),pageurl = FEED_BASE_URL % "Auvergne" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Alpes"),pageurl = FEED_BASE_URL % "Alpes" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Midi-Pyrénées"),pageurl = FEED_BASE_URL % "Midi-pyrenees" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Languedoc-Roussillon"),pageurl = FEED_BASE_URL % "Langedoc-rousillon" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Réunion"),pageurl = FEED_BASE_URL % "Reunion" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Guyane"),pageurl = FEED_BASE_URL % "Guyane" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Polynésie"),pageurl = FEED_BASE_URL % "Polynesie" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Martinique"),pageurl = FEED_BASE_URL % "Martinique" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Mayotte"),pageurl = FEED_BASE_URL % "Mayotte" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Nouvelle Calédonie"),pageurl = FEED_BASE_URL % "Nouvelle-caledonie" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Guadeloupe"),pageurl = FEED_BASE_URL % "Guadeloupe" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Wallis et Futuna"),pageurl = FEED_BASE_URL % "Wallis-et-futuna" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"Saint-Pierre et Miquelon"),pageurl = FEED_BASE_URL % "Saint-pierre-et-miquelon" ))

    return dir

def get_stream (sender,url):
    try:
      link = HTML.ElementFromURL(url).xpath('//div[@id="playerCtnr"]/a')[0].get('href')
      content = HTTP.Request(INFO_PATH + link.split('=')[-1]).content
      content = content.replace('<![CDATA[','').replace(']]>','')
      chemin = re.findall('<chemin>([^.*?]+)</chemin>',content)
      nom = re.findall('<nom>([^.*?]+)</nom>',content)
      Log(nom)
      videopath = chemin[0] + nom[0]
      Log(videopath)
      if videopath != None:
        return Redirect(WindowsMediaVideoItem(unicode(PLAYER_PATH + "/" + videopath,"utf-8")))
    except:
      return None

def get_thumb (url):
    try:
      content = HTML.ElementFromURL(url).xpath("head/meta[@name='programme_image']")
      for item in content:
        imagepath = item.get("content")
        Log(imagepath)
        if imagepath != None:
          if 'http' in imagepath:
            return DataObject(HTTP.Request(imagepath).content,'image/'+imagepath[-3:])
          else:
            return DataObject(HTTP.Request(unicode("http://www.pluzz.fr" + imagepath,"utf-8")).content,'image/'+imagepath[-3:])
        else:
          return R(ICON)
    except:
      return R(ICON)

def RSS_parser(sender, pageurl , replaceParent=False,):
    dir = MediaContainer(title2=sender.itemTitle, viewGroup="List", replaceParent=replaceParent,httpCookies=HTTP.GetCookiesForURL('http://www.pluzz.fr/'))
    rawpage = HTTP.Request(pageurl).content.replace('<![CDATA[','').replace(']]>','')
    for tag in XML.ElementFromString(rawpage,encoding = "iso-8859-1").xpath('//item'):
      Log(XML.StringFromElement(tag))
      url = 'http://www.pluzz.fr/'+tag.xpath("origlink")[0].text.split('/')[-1]
      title = tag.xpath("title",encoding = "iso-8859-1")[0].text
      if title != None:
        dir.Append(Function(VideoItem(get_stream,width=384,height=216,title=tag.xpath("title")[0].text,summary='',thumb=Function(get_thumb, url = url)),url=url))

    return dir
