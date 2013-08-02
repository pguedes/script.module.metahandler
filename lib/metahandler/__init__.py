#    metahandler XBMC Addon
#    Copyright (C) 2012 Eldorado
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
This module provides a simple API for accessing some of the basic metahandler features.

Metadata collected over time with this module will be stored in the local cache.
The local cache of metadata is kept in a local database so that it can be quickly queried while listing items in XBMC.

You will likely want to use directly the metahandlers.MetaData() class for the majority of functions.

eg.
    from metahandler import metahandlers
    metadataFacade = metahandlers.MetaData()
    metadata = metadataFacade.get_meta('movie','The Hangover',imdb_id='tt1119646')

this will first try to find the entry in the cached metadata database, and if not found will try to query the online
metadata databases (TMDB and IMDB for movies, TVDB for tv shows) to find information.
If any metadata is found for an entry, it will be updated in the cache, so that it can get quickly found on next request


The metacontainers module, is a utility module that allows importing metadata from a database with the same schema.

'''

import common

def display_settings():
    '''
    Opens the settings dialog for :mod:`metahandler`.
    
    This can be called from your addon to provide access to global 
    :mod:`metahandler` settings. 
    
    .. note::
    
        All changes made to these setting by the user are global and will 
        affect any addon that uses :mod:`metahandler`.
    '''
    common.addon.show_settings()