#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bot.document import Document
from bot.network import URLOpener
from bot.network.urls import URLParser
import yaml


def get_config(filename):
    try:
        fp = open(filename, 'r')
        data = fp.read()
        fp.close()
        return yaml.load(data)
    except IOError, e:
        print e
    return None


def main():
    conf = get_config('../conf/config.yaml')
    documents = []
    opener = URLOpener()
    parser = URLParser()
    
    sites = conf['initial']['sites']
    
    for site in sites:
        headers, data = opener.open(site)
        if headers.getheader('Content-Type').split(';')[0] == 'text/html':
            typ = parser.parse(site)
            
            doc = Document(typ[0], typ[1], typ[2], typ[3], headers, data)
            documents.append(doc)
            
            print doc.get_text()
            
            
if __name__ == '__main__':
    main()