# -*- coding: utf-8 -*-

import xbmc

from resources.lib.utils import logNot
from resources.lib.service import Setting

if __name__ == '__main__':
    logNot('Service start')
    setting = Setting()
    setting.start()
    logNot('Service stop')
    del setting
    