# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

from resources.lib.utils import logNot, setProperty, getSettingStr, getSettingInt

PROPERTY_PREFIX = 'contextmenu_item{}_'
SETTINGS_PREFIX = 'item{}_'

ENABLE = 'enable'
POSITION = 'position'
NAME = 'name'
STYLE = 'style'
COLOR = 'colour'
COMMAND = 'command'

COLOR_WHITE = '[COLOR white]'
COLOR_GREY = '[COLOR grey]'
COLOR_BLUE = '[COLOR blue]'
COLOR_GREEN = '[COLOR green]'
COLOR_YELLOW = '[COLOR yellow]'
COLOR_RED = '[COLOR red]'

COLOR_CLOSE = '[/COLOR]'

STYLE_TABLE = [['',''],['[B]','[/B]'],['[I]','[/I]'],['[B][I]','[/I][/B]']]
COLOR_TABLE = [[COLOR_WHITE,COLOR_CLOSE],[COLOR_GREY,COLOR_CLOSE],[COLOR_BLUE,COLOR_CLOSE],[COLOR_GREEN,COLOR_CLOSE],[COLOR_YELLOW,COLOR_CLOSE],[COLOR_RED,COLOR_CLOSE]]

class XBMCMonitor(xbmc.Monitor):

    def __init__(self):
        xbmc.Monitor.__init__(self)

    def onSettingsChanged(self):
        self.getSettings()

class Setting(XBMCMonitor):

    def __init__(self):
        XBMCMonitor.__init__(self)
        self.getSettings()

    def getSettings(self):
        addon = xbmcaddon.Addon()
        for i in range(1, 5):
            indexStyle = getSettingInt((SETTINGS_PREFIX + STYLE).format(i), addon)
            indexColor = getSettingInt((SETTINGS_PREFIX + COLOR).format(i), addon)
            rawName = getSettingStr((SETTINGS_PREFIX + NAME).format(i), addon)
            formatedName = COLOR_TABLE[indexColor][0] + STYLE_TABLE[indexStyle][0] + rawName + STYLE_TABLE[indexStyle][1] + COLOR_TABLE[indexColor][1]
            setProperty((PROPERTY_PREFIX + NAME).format(i), formatedName)
        logNot('Settings loaded')

    def start(self):
        i = 0
        monitor = xbmc.Monitor()
        while not monitor.abortRequested() and monitor.waitForAbort():
            i += 1
            logNot('{}'.format(i))
            pass
