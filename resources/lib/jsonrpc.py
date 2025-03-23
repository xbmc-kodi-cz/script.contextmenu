# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import sys
import re

from resources.lib.utils import localizedStr, logNot, logErr

class JSONRPC:
    VERSION = "\"jsonrpc\":\"2.0\""

def addon_control(addonId, command = restart, delay = 0, notify = false):

    command

    xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","id":1,"params":{"addonid": "pvr.iptvsimple","enabled":false}}')
