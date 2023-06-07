# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import re

from resources.lib.utils import getParam, getSettingBool, localizedStr, logNot, logErr, mediaFile
from resources.lib.patterns import selectPattern

TEXT_SEARCH_HEADER = 30051
TEXT_SEARCH_PROMPT = 30054

COMMON_BUILTIN = 'ActivateWindow(videos,plugin://{}{},return)'

SCC_ADDON = 'plugin.video.stream-cinema-2-release'
SCC_ENABLE = 'enable_search_scc'
SCC_COMMAND = '/get_media{}'
SCC_URL = '/?media_type=%2A&render_type=search&url=%252Fapi%252Fmedia%252Ffilter%252Fv2%252Fsearch%253Fvalue%253D{}%2526order%253Ddesc%2526sort%253Dscore%2526type%253D%25252A%2526size%253D50?' 

WS_ENABLE = 'enable_search_ws'
WS_COMMAND =  '/{}'
WS_URL = 'search_webshare?search_value={0}?'

SC_ADDON = 'plugin.video.stream-cinema'
SC_ENABLE = 'enable_search_sc'
SC_COMMAND = '/?url={}'
SC_URLS = [
'/Search/search-movie?search={0}&id=search-movie',
'/Search/search-people-movie?search={0}&id=search-people',
'/Search/search-series?search={0}&id=search-series',
'/Search/search-people-series?search={0}&id=search-people'
]

YT_ADDON = 'plugin.video.youtube'
YT_ENABLE = 'enable_search_yt'
YT_COMMAND = '/kodion/search/query/?{}'
YT_URL = 'q=({0})'

WHERE = 0
ADDON = 1
ENABLE = 2
TITLE = 3
SUBTITLE = 4
URL = 5
COMMAND = 6
BUILTIN = 7
ENCODE = 8

PARAMETERS = [
['scc', SCC_ADDON, SCC_ENABLE, 30055, 30056, SCC_URL, SCC_COMMAND, None, None],
['ws', SCC_ADDON, WS_ENABLE, 30057, 30058, WS_URL, WS_COMMAND, None, None],
['sc', SC_ADDON, SC_ENABLE, 30059, 30060, SC_URLS[0], SC_COMMAND, None, 'HEX'],
['sc', SC_ADDON, SC_ENABLE, 30059, 30061, SC_URLS[1], SC_COMMAND, None, 'HEX'],
['sc', SC_ADDON, SC_ENABLE, 30059, 30062, SC_URLS[2], SC_COMMAND, None, 'HEX'],
['sc', SC_ADDON, SC_ENABLE, 30059, 30063, SC_URLS[3], SC_COMMAND, None, 'HEX'],
['yt', YT_ADDON, YT_ENABLE, 30064, 30065, YT_URL, YT_COMMAND, None, None]
]

def getText(default, title):
    keyboard = xbmc.Keyboard(default, title, False)
    keyboard.doModal()
    text = keyboard.getText().strip()
    return keyboard.isConfirmed() and len(text) > 0, text

def nothingToDo():
    logNot('Search - Nothing to do')

def parametersInit(parameters):
    params = []
    for param in parameters:
        try:
            addon = xbmcaddon.Addon(param[ADDON])
        except:
            continue
        else:
            if not getSettingBool(param[ENABLE]):
                continue
            params.append(param)
    return params

def setUrl(value, url = None, addon = None, encode = None):
    if url == None:
        url = COMMON_BUILTIN
    if encode == None:
        if addon == None:
            return url.format(value)
        else:
            return url.format(addon, value)
    if encode == 'HEX':
        return url.format(value).encode("utf-8").hex()
    else:
        logErr('Unknown encode format: {}'.format(encode))

if __name__ == '__main__':
    whereToSearch = getParam(1)
    logNot('whereToSearch: {}'.format(whereToSearch))
    parameters = parametersInit(PARAMETERS)
    goSearch, searchString = getText(selectPattern(), localizedStr(TEXT_SEARCH_PROMPT))
    if goSearch:
        dialog = xbmcgui.Dialog()
        if getSettingBool('common_item_search'):
            items=[]
            for parameter in parameters:
                label = localizedStr(parameter[TITLE])
                label2 = localizedStr(parameter[SUBTITLE])
                item = xbmcgui.ListItem(label=label, label2=label2)
                item.setArt({'icon': mediaFile(parameter[WHERE], 'png')})
                items.append(item)
            select = dialog.select('Hledat...', items, useDetails = True)
        else:
            # parameters = list(filter(lambda p: p[0] == whereToSearch, parameters))
            parameters = list([p for p in parameters if p[0] == whereToSearch])
            lenght = len(parameters)
            if lenght > 1:
                select = dialog.select(localizedStr(parameters[0][TITLE]), [localizedStr(parameter[SUBTITLE]) for parameter in parameters])
            else:
                select = lenght - 1
        goSearch = select != -1
        if goSearch:
            logNot('Select: {}'.format(select))
            parameter = parameters[select]
            searchUrl = setUrl(searchString, parameter[URL], encode = parameter[ENCODE])
            addonCommand = setUrl(searchUrl, parameter[COMMAND])
            builtinCommand = setUrl(addonCommand, parameter[BUILTIN], parameter[ADDON])
            logNot('Start search based on the builtin command: {}'.format(builtinCommand))
            xbmc.executebuiltin(builtinCommand)
        else:
            nothingToDo()
    else:
        nothingToDo()
