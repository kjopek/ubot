#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen
from requests import get

class URLOpener(object):
    '''
    Klasa do otwierania różnego rodzaju url-i.
    
    Domyślnie przedstawia się stronom jako 'Pandora/0.02'
    '''
    
    def __init__(self, user_agent='Pandora/0.02'):
        self.user_agent = user_agent
    
        
    def open(self, url):
        #request = Request(url)
        #request.add_header('User-Agent', self.user_agent)
        #response = urlopen(request)
        
        # return headers, data
        response = get(url)
        return response.headers, response.text