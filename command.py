# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

from resources.lib.utils import getParam, getSettingStr

if __name__ == '__main__':
    command = getParam(1).split(',')[0]
    if command[0] == '@':
        command = getSettingStr(command[1:])
    xbmc.executebuiltin(command)
