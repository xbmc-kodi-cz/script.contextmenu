# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui

from resources.lib.utils import logNot, logErr, notification

def getAddonId():
    addonId = xbmc.getInfoLabel('Container.PluginName')
    logNot(addonId)
    return addonId

def addonRestart():
    addonId = getAddonId()
    addonId = 'pvr.hts'
    try:
        xbmc.executeJSONRPC('{{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{{"addonid":"{}","enabled":false}}}}'.format(addonId))
        logNot('addon: {} stopped'.format(addonId))
        xbmc.sleep(3000)
        xbmc.executeJSONRPC('{{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{{"addonid":"{}","enabled":true}}}}'.format(addonId))
        logNot('addon: {} started'.format(addonId))
    except:
        pass

if __name__ == '__main__':
    logNot('Addon restart')
    addonRestart()

    # addonId = xbmc.getInfoLabel('Container.PluginName')
    # logNot('addonId: {}'.format(addonId))
    # pluginCategory = xbmc.getInfoLabel('Container.PluginCategory')
    # logNot('pluginCategory: {}'.format(pluginCategory))
    # folderName = xbmc.getInfoLabel('Container.FolderName')
    # logNot('folderName: {}'.format(folderName))
    # folderPath = xbmc.getInfoLabel('Container.FolderPath')
    # logNot('folderPath: {}'.format(folderPath))
    # fileName = xbmc.getInfoLabel('ListItem.FileName')
    # logNot('fileName: {}'.format(fileName))
    # path = xbmc.getInfoLabel('ListItem.Path')
    # logNot('path: {}'.format(path))
    # fileNameAndPath = xbmc.getInfoLabel('ListItem.FileNameAndPath')
    # logNot('fileNameAndPath: {}'.format(fileNameAndPath))

    # addon = xbmcaddon.Addon(addonId)
    # addon.openSettings()
    # xbmc.executebuiltin('Container.Refresh()')
    