#-*- coding: utf-8 -*-
#Venom.
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.config import cConfig
from resources.lib.parser import cParser
from resources.lib.util import cUtil

SITE_IDENTIFIER = 'filmstreamingz_fr'
SITE_NAME = 'Filmstreaming.cc et Streamingserie.tv'
SITE_DESC = 'Film Streaming & Serie Streaming'

URL_MAIN = 'http://filmstreaming.cc/'
URL_MAIN2 = 'http://streamingserie.tv/'

MOVIE_MOVIE = (URL_MAIN, 'showMovies')
MOVIE_NEWS = (URL_MAIN, 'showMovies')
MOVIE_VIEWS = (URL_MAIN + 'les-plus-vus/', 'showMovies')
MOVIE_COMMENTS = (URL_MAIN + 'les-plus-commentes-2/', 'showMovies')
MOVIE_NOTES = (URL_MAIN + 'les-mieux-notes-2/', 'showMovies')
MOVIE_GENRES = (True, 'showGenre')

SERIE_SERIES = (URL_MAIN2, 'showMovies')
SERIE_NEWS = (URL_MAIN2, 'showMovies')

URL_SEARCH = (URL_MAIN + '?s=', 'showMovies')
FUNCTION_SEARCH = 'showMovies'

def load(): 
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showMoviesSearch', 'Films Recherche', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films Nouveautés', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VIEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VIEWS[1], 'Films Les Plus Vus', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_COMMENTS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_COMMENTS[1], 'Films Les Plus Commentés', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NOTES[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NOTES[1], 'Films Les Mieux Notés', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', 'Films Genres', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeriesSearch', 'Series Recherche', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Series Nouveautés', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN2 + 'les-plus-vues/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Series Les Plus Vues', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN2 + 'les-plus-commentees/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Series Les Plus Commentés', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN2 + 'les-mieux-notees/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Series Les Mieux Notées', 'series.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()

def showMoviesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = URL_MAIN + '?s='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return
    

def showSeriesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = URL_MAIN2 + '?s='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return
    


def showGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    liste = []

    liste.append( ['Action',URL_MAIN + 'category/action/'] )
    liste.append( ['Afro',URL_MAIN + 'category/afro/'] )
    liste.append( ['Animation',URL_MAIN + 'category/animation/'] )
    liste.append( ['Arts Martiaux',URL_MAIN + 'category/arts-martiaux/'] )
    liste.append( ['Aventure',URL_MAIN + 'category/aventure/'] )
    liste.append( ['Comedie',URL_MAIN + 'category/comedie/'] )
    liste.append( ['Documentaire',URL_MAIN + 'category/documentaire/'] )
    liste.append( ['Drame',URL_MAIN + 'category/drame/'] )
    liste.append( ['Espionnage',URL_MAIN + 'category/espionnage/'] )
    liste.append( ['Famille',URL_MAIN + 'category/famille/'] )
    liste.append( ['Fantastique',URL_MAIN + 'category/fantastique/'] )
    liste.append( ['Guerre',URL_MAIN + 'category/guerre/'] )
    liste.append( ['Historique',URL_MAIN + 'category/historique/'] )
    liste.append( ['Epouvante-Horreur',URL_MAIN + 'category/horreur/'] )
    liste.append( ['Musical',URL_MAIN + 'category/musical/'] )
    liste.append( ['Policier',URL_MAIN + 'category/policier/'] )
    liste.append( ['Romance',URL_MAIN + 'category/romance/'] )
    liste.append( ['Science-Fiction',URL_MAIN + 'category/science-fiction/'] )
    liste.append( ['Spectacle',URL_MAIN + 'category/spectacle/'] )
    liste.append( ['Thriller',URL_MAIN + 'category/thriller/'] )
    liste.append( ['Western',URL_MAIN + 'category/western/'] )

    for sTitle,sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showMovies(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    
    if sSearch:
        sUrl = sSearch
      
        sDisp = oInputParameterHandler.getValue('disp')
        if (sDisp == 'search2'):#serie
            sUrl = sUrl.replace(URL_MAIN,URL_MAIN2)
            
        sUrl = sUrl.replace('%20','+')
      
    else:
        sUrl = oInputParameterHandler.getValue('siteUrl')
        
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('//ad.advertstream.com/', '').replace('http://www.adcash.com/', '').replace('http://regie.espace-plus.net/', '')
    sPattern = '<div class="moviefilm"> *<a href=".+?"> *<img src="([^<]+)" alt=".+?" height=".+?" width=".+?" \/><\/a><div class="movief"><a href="([^<]+)">([^<]+)<\/a><\/div><div class="movies"><small>(.+?)<\/small>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            sSmall = aEntry[3].replace('<span class="likeThis">', '').replace('</span>', '')
            sTitle = aEntry[2]+' - [COLOR azure]'+sSmall+'[/COLOR]'
            
            sDisplayTitle = cUtil().DecoTitle(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[1]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(aEntry[2]))
            oOutputParameterHandler.addParameter('sThumbnail', str(aEntry[0]))
            if URL_MAIN2 in sUrl:
                oGui.addTV(SITE_IDENTIFIER, 'showSeries', sDisplayTitle, '', aEntry[0], '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', aEntry[0], '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def showSeries():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl = sUrl+'100/'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<a href="([^<]+)"><span>(.+?)</span></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = sMovieTitle+' - '+aEntry[1]
            
            sDisplayTitle = cUtil().DecoTitle(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    sPattern = '<span class=\'current\'>.+?</span><a class="page larger" href="(.+?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False


def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<iframe src="//www.facebook.com/','')


    sPattern = '<iframe.+?src=[\'|"](.+?)[\'|"]'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            sHosterUrl = str(aEntry)

            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()


def serieHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    sPattern = 'href="([^<]+)" target="_blank">.+?</a>'
    oParser = cParser()
    aResult = oParser.parse(sUrl, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            sHosterUrl = str(aEntry)
            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
