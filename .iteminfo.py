# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

from resources.lib.utils import logNot
# from iteminfo.script import Gui
from iteminfo.script import Gui as script

# if __name__ == '__main__':
    # xbmc.executebuiltin('ActivateWindow(1150)')

if __name__ == '__main__':
    logNot('Script start')
    itemInfo = script.Gui('iteminfo.xml', xbmcaddon.Addon().getAddonInfo('path'), 'default', '1080i')
    itemInfo.doModal()
    logNot('Script stop')
    del itemInfo
        