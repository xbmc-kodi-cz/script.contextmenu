# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui

from resources.lib.utils import logNot, logErr, notification

if __name__ == '__main__':
    logNot('Addon restart')
    addonId = 'pvr.hts'
    xbmc.executeJSONRPC('{{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{{"addonid":"{}","enabled":false}}}}'.format(addonId))
    logNot('addon: {} stopped'.format(addonId))
    xbmc.sleep(3000)
    xbmc.executeJSONRPC('{{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{{"addonid":"{}","enabled":true}}}}'.format(addonId))
    logNot('addon: {} started'.format(addonId))
