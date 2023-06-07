# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

if __name__ == '__main__':
    addonId = xbmc.getInfoLabel('Container.PluginName')
    addon = xbmcaddon.Addon(addonId)
    addon.openSettings()
    xbmc.executebuiltin('Container.Refresh()')
    