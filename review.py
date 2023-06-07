# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import sys

item = sys.listitem

info = item.getVideoInfoTag()

title = info.getTitle()
year = info.getYear()
plot = info.getPlotOutline()

xbmcgui.Window(10000).setProperty('TextViewer_Header', 'Recenze: ' + title + ' (' + str(year) + ')')
xbmcgui.Window(10000).setProperty('TextViewer_Text', plot)

xbmc.executebuiltin('ActivateWindow(1102)')
