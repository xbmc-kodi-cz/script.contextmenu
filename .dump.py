# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon

from resources.lib.utils import logNot

def dump(item):
    logNot('{}: {}'.format(item, xbmc.getInfoLabel(item)))

if __name__ == '__main__':
    logNot('***********************************')
    dump('Container.PluginName')
    dump('Container.PluginCategory')
    dump('Container.FolderName')
    dump('Container.FolderPath')
    dump('ListItem.TVShowTitle')
    dump('ListItem.Title')
    dump('ListItem.OriginalTitle')
    dump('ListItem.Label')
    dump('ListItem.FileName')
    dump('ListItem.Path')
    dump('ListItem.FileNameAndPath')
    logNot('***********************************')
