# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import sys

from resources.lib.utils import logNot

addon = xbmcaddon.Addon()
player = xbmc.Player()

item = sys.listitem
info = item.getVideoInfoTag()
icon = item.getArt('thumb')
trailer = info.getTrailer()
title = info.getTitle()

item = xbmcgui.ListItem('')
item.setInfo('video', { 'title': title + ' (' + addon.getLocalizedString(30021) + ')' })
item.setArt({ 'thumb': icon, 'icon': icon })
player.play(trailer, item)
