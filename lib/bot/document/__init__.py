# -*- coding: utf-8 -*-
import hashlib
from BeautifulSoup import BeautifulSoup

class IncorrectContentError(Exception):
    pass

class Document(object):
    
    SUPPORTED_CONTENTS = ['text/html']

    
    def __init__(self, protocol, secure, sitename, location, headers, data):
        self.protocol = protocol
        self.secure = secure
        self.sitename = sitename
        self.location = location

        content_type = headers['Content-Type'].split(';')[0]

        if content_type not in self.SUPPORTED_CONTENTS:
            raise IncorrectContentError(content_type)

        self.headers = headers
        self.data = unicode(data)
        
        self.hash = self.hashme()
        
    
    def hashme(self):
        if not hasattr(self, '_calculated_hash'):
            sha256 = hashlib.new('sha256')
            sha256.update(self.data.encode("utf-8"))
            self._calculated_hash = sha256.digest()
        return self._calculated_hash
    
    
    def pretty_hash(self):
        return ''.join(['%02x' % ord(v) for v in self.hashme()])
    
    
    def __str__(self):
        return ('Name:       %s\n'
                '  Protocol: %s\n'
                '  Location: %s\n'
                '  Hash:     %s\n'
                '  Data len: %d\n') % (self.sitename, self.protocol,
                                 self.location, self.pretty_hash(),
                                 len(self.data))
                 
                 
    def __eq__(self, other):
        assert type(other) == Document, 'You cannot compare Document to other types'
        
        site1 = self.sitename.replace('www.', '') if self.sitename.startswith('www.') else self.sitename
        site2 = other.sitename.replace('www.', '') if other.sitename.startswith('www.') else other.sitename
        
        if site1 == site2:
            return True
        else:
            return self.hash == other.hash

    
    def get_elements(self, name, attrs=None):
        bs = BeautifulSoup(self.data, convertEntities=BeautifulSoup.HTML_ENTITIES)
        return bs.findAll(name, attrs)
    
    
    def get_text(self):
        bs = BeautifulSoup(self.data, convertEntities=BeautifulSoup.HTML_ENTITIES)
        return ''.join(bs.body(text=True))
    
    
    def __hash__(self):
        return id(self.hashme())