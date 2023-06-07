# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

if __name__ == '__main__':
    addon = xbmcaddon.Addon('plugin.video.stream-cinema-2-release')
    addon.openSettings()
    xbmc.executebuiltin('Container.Refresh()')
