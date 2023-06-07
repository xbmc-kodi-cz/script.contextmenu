# -*- coding: utf-8 -*-

import xbmcaddon

from resources.lib.utils import getParam

if __name__ == '__main__':
    args = getParam(1).split(',')
    addon = xbmcaddon.Addon(args[0]) 
    addon.setSettingBool(args[1], True if args[2].lower() == 'true' else False)
