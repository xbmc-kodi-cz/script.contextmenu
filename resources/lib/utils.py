# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs

import os
import sys

addon = xbmcaddon.Addon()
addonId = addon.getAddonInfo('id')
addonName = addon.getAddonInfo('name')
addonLang = addon.getLocalizedString
addonVersion = addon.getAddonInfo('version')
addonPath = xbmcvfs.translatePath(addon.getAddonInfo('path'))
addonProfile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
addonIcon = xbmcvfs.translatePath(os.path.join(addonPath, 'resources', 'icon.png'))
addonMedia = xbmcvfs.translatePath(os.path.join(addonPath, 'resources', 'media'))

TRUE = 'TRUE'
FALSE = 'FALSE'

TRACKING = True

def log(message, level=xbmc.LOGINFO):
    xbmc.log('[%s] %s' % (addonName, message), level)

def logNot(message):
    log(message,level=xbmc.LOGINFO)

def logWrn(message):
    log(message,level=xbmc.LOGWARNING)

def logDbg(message):
    log(message,level=xbmc.LOGDEBUG)

def logErr(message):
    log(message,level=xbmc.LOGFATAL)
    
def logTracking(message):
    if TRACKING:
        log('[TRACKING] %s' % message,level=xbmc.LOGNOTICE)

def notification(message, icon=addonIcon, time=5000):
    if icon == 'INFO':
        icon = xbmcgui.NOTIFICATION_INFO
    elif icon == 'WARNING':
        icon = xbmcgui.NOTIFICATION_WARNING
    elif icon == 'ERROR':
        icon = xbmcgui.NOTIFICATION_ERROR
    xbmc.executebuiltin('XBMC.Notification(%s,%s,%i,%s)' % (addonName, message, time, icon))

def getParam(param):
    if len(sys.argv) > param:
        return sys.argv[param]
    else:
        return ''

def getSettingBool(param, addon = xbmcaddon.Addon()):
    return True if addon.getSetting(param).upper() == TRUE else False

def getSettingInt(param, addon = xbmcaddon.Addon()):
    return int(addon.getSetting(param))

def getSettingNumber(param, addon = xbmcaddon.Addon()):
    return float(addon.getSetting(param))

def getSettingStr(param, addon = xbmcaddon.Addon()):
    return addon.getSetting(param)
    
def getLocalizedStr(addon, label):
    return xbmcaddon.Addon(addon).getLocalizedString(label)
    
def localizedStr(label, addon = xbmcaddon.Addon()):
    return addon.getLocalizedString(label)
    
def getProperty(variable, window = 10000):
    return xbmcgui.Window(window).getProperty(variable)

def setProperty(variable, value, window = 10000):
    xbmcgui.Window(window).setProperty(variable, value)

def clearProperty(variable, window = 10000):
    xbmcgui.Window(WINDOW_HOME).clearProperty(variable)

def clearProperties(variables, window = 10000):
    for variable in variables:
        clearProperty(variable, window)

def mediaFile(name, suffix, path = addonMedia):
    return '{}/{}.{}'.format(path, name, suffix)
