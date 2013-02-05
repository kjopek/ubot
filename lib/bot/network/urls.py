'''
Created on 21-08-2012

@author: kj
'''

import re

class URLParser(object):
    '''
    Class for parsing and classifying urls.
    '''
    
    URL_TYPES = {
             'global'   : re.compile(r'^http(s)?://'),
             'relative' : re.compile(r'^/([^\/]+)'),
             'main'     : re.compile(r'^\/$'),
             'id'       : re.compile(r'^[#](.+)?'),
             'local'    : re.compile(r'^(?!(http(s)?|[/#]))(.*)$')
             }

    URL_PARSE = re.compile(r'(?P<protocol>((http)|(ftp)|(mail)))(?P<secure>(s?))://(?P<sitename>[^/]+)(?P<document>(\/(.*)))?')


    def __init__(self):
        pass
    
    
    def parse(self, url):
        matched = self.URL_PARSE.match(url)
        name = matched.group('sitename')
        
        try:
            protocol = matched.group('protocol')
        except IndexError:
            protocol = 'http'
        
        try:
            if matched.group('secure'):
                secure = True
            else:
                secure = False
        except IndexError: 
            secure = False
        
        try:
            document = matched.group('document')
            if document is not None:
                document.replace('//', '/')
            else:
                document = '/'
                
        except IndexError:
            document = '/'
        
        return (protocol, secure, name, document)


    
    def join(self, current_site, document=True):
        if document:
            return '%s%s://%s%s' % (current_site[0], 
                                    's' if current_site[1] else '', 
                                    current_site[2], 
                                    '' if not current_site[3] else current_site[3])
        else:
            return  '%s%s://%s' % (current_site[0], 
                                   's' if current_site[1] else '', 
                                   current_site[2])   


    def get_type(self, url):
        for name,pattern in self.URL_TYPES.iteritems():
            if pattern.match(url):
                return name