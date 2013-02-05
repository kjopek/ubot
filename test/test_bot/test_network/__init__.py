from bot.network.urls import URLParser
from unittest import TestCase

class URLParserTest(TestCase):
    
    TEST_URLS = {
                 'http://www.onet.pl/' : ('http', False, 'www.onet.pl', '/'),
                 'https://gmail.com/' : ('http', True, 'gmail.com', '/'),
                 'ftp://ftp.task.gda.pl/' : ('ftp', False, 'ftp.task.gda.pl', '/')
                 }
    
    TEST_URLS_TYPE = {
                      'http://onet.pl' : 'global',
                      '/test.php?a=1' : 'relative',
                      '/' : 'main',
                      '#/soma/fb/path' : 'id',
                      'test.php?a=3' : 'local'
                      }
    
    def setUp(self):
        self.parser = URLParser()
        
    def test_parse(self):
        for url, cls in self.TEST_URLS.iteritems():
            self.assertEquals(self.parser.parse(url), cls)
            
    def test_join(self):
        for url, cls in self.TEST_URLS.iteritems():
            self.assertEquals(self.parser.join(cls), url)
            
    def test_get_type(self):
        for url, type in self.TEST_URLS_TYPE.iteritems():
            self.assertEquals(type, self.parser.get_type(url))