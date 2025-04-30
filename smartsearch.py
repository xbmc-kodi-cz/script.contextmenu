# -*- coding: utf-8 -*-

import xbmc

from urllib.parse import quote

from resources.lib.utils import getParam, getSettingBool, localizedStr, logNot, logErr

COMMON_BUILTIN = 'ActivateWindow(videos,"plugin://{}{}",return)'

YAWSP_ADDON = 'plugin.video.yawsp'
YAWSP_ENABLE = 'enable_search_yawsp'
YAWSP_COMMAND = '{}'
YAWSP_URL = '/?action=search&what={}'

def nothingToDo():
    logNot('Search - Nothing to do')
    
def setUrl(value, url = None, addon = None):
    if url == None:
        url = COMMON_BUILTIN
    if addon == None:
        return url.format(value)
    else:
        return url.format(addon, value)

if __name__ == '__main__':
    howToSearch = getParam(1)
    if howToSearch == 'default':
        logNot('howToSearch: {}'.format(howToSearch))
        item = sys.listitem
        info = item.getVideoInfoTag()
        dbType = xbmc.getInfoLabel('ListItem.DBTYPE')
        logNot('DBTYPE: {}'.format(dbType))
        goSearch = True
        if dbType == 'movie':
            searchString = xbmc.getInfoLabel('ListItem.Title')
        elif dbType == 'tvshow':
            searchString = xbmc.getInfoLabel('ListItem.TVShowTitle')
        elif dbType == 'season':
            searchString = '{0} S{1:02d}'.format(xbmc.getInfoLabel('ListItem.TVShowTitle'), int(xbmc.getInfoLabel('ListItem.Season')))
        elif dbType == 'episode':
            searchString = '{0} S{1:02d}E{2:02d}'.format(xbmc.getInfoLabel('ListItem.TVShowTitle'), int(xbmc.getInfoLabel('ListItem.Season')), int(xbmc.getInfoLabel('ListItem.Episode')))
        else:
            goSearch = False
        if goSearch:
            searchUrl = setUrl(quote(searchString), YAWSP_URL)
            logNot('searchUrl: {}'.format(searchUrl))
            addonCommand = setUrl(searchUrl, YAWSP_COMMAND)
            logNot('addonCommand: {}'.format(addonCommand))
            builtinCommand = setUrl(addonCommand, COMMON_BUILTIN, YAWSP_ADDON)
            logNot('Start search based on the builtin command: {}'.format(builtinCommand))
            xbmc.executebuiltin(builtinCommand)
        else:
            nothingToDo()
    else:
        nothingToDo()
