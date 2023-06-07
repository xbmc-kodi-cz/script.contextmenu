# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import re

from resources.lib.utils import logNot, logErr

if __name__ == '__main__':
    path = xbmc.getInfoLabel('ListItem.Path')
    parsed = re.match('plugin\://([^/]*)/.*', path)
    addonId = parsed.group(1)
    if len(addonId) == 0:
        logNot('Nothig to do')
    else:
        try:
            addon = xbmcaddon.Addon(addonId)
            addon.openSettings()
            xbmc.executebuiltin('Container.Refresh()')
        except:
            logErr('Parse error')
