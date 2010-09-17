# -*- coding: utf-8 -*-
from PMS import *
from PMS.Objects import *
from PMS.Shortcuts import *

####################################################################################################

PLUGIN_PREFIX           = "/video/francetelevisions"
PLUGIN_ID               = "com.plexapp.plugins.francetelevisions"
PLUGIN_REVISION         = 0.6
PLUGIN_UPDATES_ENABLED  = True

PLAYER_PATH = "mms://a988.v101995.c10199.e.vm.akamaistream.net/7/988/10199/3f97c7e6/ftvigrp.download.akamai.com/10199/cappuccino/production/publication/"

NAME = L('France Televisions')

ART           = 'art-default.png'
ICON          = 'icon-default.png'

FEED_BASE_URL = "http://feeds.feedburner.com/Pluzz-%s?format=xml"
LOGO_URL = "http://www.francetelevisions.fr/images/france%s_logo.gif"

####################################################################################################

def Start():

    Plugin.AddPrefixHandler(PLUGIN_PREFIX, VideoMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
    Plugin.AddViewGroup("Coverflow", viewMode="Coverflow", mediaType="items")

    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    DirectoryItem.thumb = R(ICON)

def VideoMainMenu():

    dir = MediaContainer(viewGroup="List")

    dir.Append(Function(DirectoryItem(RSS_parser,"Tous les programmes"),pageurl = "http://www.pluzz.fr/rss" ))
    dir.Append(Function(DirectoryItem(ChannelSubMenu,"Par chaîne")))
    dir.Append(Function(DirectoryItem(GenreSubMenu,"Par genre")))
    dir.Append(Function(DirectoryItem(RegionSubMenu,"Par région")))
    
    return dir

def ChannelSubMenu (sender):
    dir = MediaContainer(title2="Chaînes", viewGroup="Coverflow")

    dir.Append(Function(DirectoryItem(RSS_parser,"France2",thumb=LOGO_URL % '2'),pageurl = FEED_BASE_URL % "France2" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France3",thumb=LOGO_URL % '3'),pageurl = FEED_BASE_URL % "France3" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France4",thumb=LOGO_URL % '4'),pageurl = FEED_BASE_URL % "France4" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"France5",thumb=LOGO_URL % '5'),pageurl = FEED_BASE_URL % "France5" ))
    dir.Append(Function(DirectoryItem(RSS_parser,"FranceO",thumb=LOGO_URL % 'O'),pageurl = FEED_BASE_URL % "FranceO" ))

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

def get_stream (url):
    try:
      link = XML.ElementFromURL(url,True).xpath('//div[@id="playerCtnr"]/a')[0].get('href')
      content = XML.ElementFromURL(link,True).xpath("head/meta[@name='urls-url-video']")
      for item in content:
        videopath = item.get("content")
        if videopath != None:
          name = unicode(PLAYER_PATH + "/" + videopath,"utf-8")
        else:
          content = XML.ElementFromURL(link,True).xpath("head/meta[@name='vignette-type-lien-externe-url']")
          for item in content:
            videopath = item.get("content")
            if videopath != None:
              name = unicode(videopath,"utf-8")
            else:
              return (None, None)
        
      content = XML.ElementFromURL(url,True).xpath("head/meta[@name='programme_image']")
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
    dir = MediaContainer(title2=sender.itemTitle, viewGroup="List", replaceParent=replaceParent)
    for tag in XML.ElementFromURL(pageurl).xpath('//item'):
      (stream , vignette) = get_stream(unicode(tag.xpath("link")[0].text,"utf-8"))
      if stream != None:
        dir.Append(WindowsMediaVideoItem(stream,width=384,height=216,title=tag.xpath("title")[0].text,summary='',thumb=vignette))

    return dir
