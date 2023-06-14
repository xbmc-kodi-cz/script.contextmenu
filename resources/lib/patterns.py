# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import sys
import re

from resources.lib.utils import localizedStr, logNot, logErr

TEXT_SELECT_PATTERN = 30053
TEXT_GENRE = 30085
TEXT_DIRECTOR = 30086
TEXT_WRITER = 30087
TEXT_CAST = 30088
TEXT_AS = 30089

# Just for the test, if it will be useful, it will be defined in the language texts of the addon too.
ROLES = [
'Arranger',
'Composer',
'Conductor',
'DJMixer',
'Engineer',
'Lyricist',
'Mixer',
'Orchestra',
'Producer',
'Remixer'
 ]

patterns = []
patternList = []

patternMask = [
re.compile('(\[COLOR lightskyblue\].* · \[/COLOR\])|(\[LIGHT\].*\[/LIGHT\])*'), # SCC
re.compile(' - \[B\].*'), # SC
re.compile('\[COLOR blue\].*\[/COLOR\] · ') # Internet TV
]

def textCleaning(text):
    if len(text) == 0:
        return ''
    for pattern in patternMask:
        text = pattern.sub('', text)
    return text.strip()

def _textCleaning(text):
    if len(text) == 0:
        return ''
    path = xbmc.getInfoLabel('ListItem.Path')
    if path.startswith('plugin://plugin.video.stream-cinema-2-release'):
        logNot('Search - SCC tags cleaning')
        text = re.sub('(\[COLOR lightskyblue\].* · \[/COLOR\])|(\[LIGHT\].*\[/LIGHT\])*','',text)
    elif path.startswith('plugin://plugin.video.stream-cinema'):
        logNot('Search - SC tags cleaning')
        text = re.sub(' - \[.*','',text)
    else:
        logNot('Search - Nothing to cleaning')
    return text.strip()

def append(item):
    patterns.append(item)
    patternList.append(item)

def addString(pattern, unique = True):
    if not (pattern in patterns and unique) and len(pattern) > 0:
        append(pattern)

def addYear(pattern):
    if pattern > 0:
        append(str(pattern))

def addImdb(pattern):
    if len(pattern) > 0:
        imdb = 'tt{}'.format(pattern)
        patterns.append(imdb)
        patternList.append('[I]IMDB:[/I]  {}'.format(imdb))

def addEpisode(season, episode):
    if season >= 0 and episode >= 0:
        append('{}x{:02d}'.format(season, episode))

def addPrefixedString(pattern, prefix):
    if len(pattern) > 0:
        patternPrefixed = '[I]{}:[/I]  {}'.format(prefix, pattern)
        if patternPrefixed not in patternList:
            patterns.append(pattern)
            patternList.append(patternPrefixed)

def addPrefixedActorString(pattern, prefix):
    if len(pattern.getName()) > 0:
        patterns.append(pattern.getName())
        if len(pattern.getRole()) > 0:
            patternList.append('[I]{}:[/I]  {}  [I]{} {}[/I]'.format(prefix, pattern.getName(), localizedStr(TEXT_AS), pattern.getRole()))
        else:
            patternList.append('[I]{}:[/I]  {}'.format(prefix, pattern.getName()))

def unique(items):
    uniqueItems = []
    for item in items:
        if item not in uniqueItems:
            uniqueItems.append(item)
    return uniqueItems

def setUrl(value, url = None, addon = None, encode = None):
    if url == None:
        url = COMMON_BUILTIN
    if encode == None:
        if addon == None:
            return url.format(value)
        else:
            return url.format(addon, value)
    if encode == 'HEX':
        return url.format(value).encode("utf-8").hex()
    else:
        logErr('Unknown encode format: {}'.format(encode))

def selectPattern():
    item = sys.listitem
    info = item.getVideoInfoTag()
    
    addString(textCleaning(info.getTVShowTitle()))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Album')))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Title')))
    addString(textCleaning(info.getTitle()))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Label')))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Title')))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.EpisodeName')))
    addString(textCleaning(info.getOriginalTitle()))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.OriginalTitle')))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Artist')))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.AlbumArtist')))
    addEpisode(info.getSeason(), info.getSeason())
    addYear(info.getYear())
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Year')))
    addImdb(info.getIMDBNumber())
    for genre in info.getGenres():
        addPrefixedString(genre, localizedStr(TEXT_GENRE))
    addPrefixedString(xbmc.getInfoLabel('ListItem.Genre'), localizedStr(TEXT_GENRE))
    for director in info.getDirectors():
        addPrefixedString(director, localizedStr(TEXT_DIRECTOR))
    for writer in info.getWriters():
        addPrefixedString(writer, localizedStr(TEXT_WRITER))
    addPrefixedString(xbmc.getInfoLabel('ListItem.Writer'), localizedStr(TEXT_WRITER))
    for role in ROLES:
        addPrefixedString(xbmc.getInfoLabel('ListItem.Property(Role.{})'.format(role)), role)
    for actor in info.getActors():
        addPrefixedActorString(actor, localizedStr(TEXT_CAST))

    # logNot('ListItem.Artist: {}'.format(xbmc.getInfoLabel('ListItem.Artist')))
    # logNot('ListItem.Cast: {}'.format(xbmc.getInfoLabel('ListItem.Cast')))
    # logNot('ListItem.CastAndRole: {}'.format(xbmc.getInfoLabel('ListItem.CastAndRole')))

    dialog = xbmcgui.Dialog()
    select = dialog.multiselect(localizedStr(TEXT_SELECT_PATTERN), patternList)
    logNot('Select: {}'.format(str(select)))
    
    pattern = ''
    if select == None:
        return pattern
    selectedPatterns = []
    for item in select:
        selectedPatterns.append(patterns[item])
    for selectedPattern in unique(selectedPatterns):
        pattern = pattern + '{} '.format(selectedPattern)
    return pattern.strip()

def buildYtPattern():
    tempPattern = ''
    item = sys.listitem
    info = item.getVideoInfoTag()

    def addString(pattern, unique = True):
        if not (pattern in patterns and unique) and len(pattern) > 0:
            patterns.append(pattern)

    addString(textCleaning(info.getTVShowTitle()))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Title')))
    addString(textCleaning(info.getTitle()))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Label')))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.Title')))
    addString(textCleaning(info.getOriginalTitle()))
    addString(textCleaning(xbmc.getInfoLabel('ListItem.OriginalTitle')))
    for pattern in patterns:
        tempPattern = tempPattern + '{} '.format(pattern)
    pattern = ('{} trailer teaser'.format(tempPattern.strip()))
    # logNot('Pattern: {}'.format(pattern))

    return pattern.strip()
