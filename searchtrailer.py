# -*- coding: utf-8 -*-

import xbmc
# import xbmcaddon
# import xbmcgui
# import re

from resources.lib.utils import logNot
from resources.lib.patterns import buildYtPattern, setUrl

COMMON_BUILTIN = 'ActivateWindow(videos,plugin://{}{},return)'

YT_ADDON = 'plugin.video.youtube'
YT_ENABLE = 'enable_search_yt'
YT_COMMAND = '/kodion/search/query/?{}'
YT_URL = 'q=({0})'

def nothingToDo():
    logNot('Search - Nothing to do')

if __name__ == '__main__':
    searchString = buildYtPattern()
    if len(searchString) > 0:
        searchUrl = setUrl(searchString, YT_URL)
        addonCommand = setUrl(searchUrl, YT_COMMAND)
        builtinCommand = setUrl(addonCommand, COMMON_BUILTIN, YT_ADDON)
        logNot('Start search based on the builtin command: {}'.format(builtinCommand))
        xbmc.executebuiltin(builtinCommand)
    else:
        nothingToDo()
