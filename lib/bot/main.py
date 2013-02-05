# -*- coding: utf-8 -*-

from bot.db import BotDB
from bot.document import Document
from bot.network import URLOpener
from bot.network.urls import URLParser
from bot.utils import global_exc_handler

import logging.config

import sys
import yaml


class Bot:
    def __init__(self):
        self.conf = self.get_config('conf/config.yaml')
        logging.config.dictConfig(self.conf['logging'])
        
        sys.excepthook = global_exc_handler
        
        self.logger = logging.getLogger("main")
        self.logger.info("Starting up...")
    
    def get_config(self, filename):
        try:
            fp = open(filename, 'r')
            data = fp.read()
            fp.close()
            return yaml.load(data)
        except IOError, e:
            print e
        raise Exception("Cannot load configuration")
    
    
    def main(self):
        
        documents = []
        queue = []
        opener = URLOpener()
        parser = URLParser()
        db = BotDB(self.conf)
        parsed = []
        
        queue += self.conf['initial']['sites']
        print queue
        
        while len(queue) > 0:
            site = queue.pop(0)
            
            if site in parsed:
                continue
    
            parsed.append(site)
            self.logger.info("Parsing site: {0}".format(site))
            self.logger.info("Len of queue: {0}".format(len(queue)))
            headers, data = opener.open(site)
            
            if 'Content-Type' in headers:
                if headers['Content-Type'].split(';')[0] == 'text/html':
                    quad = parser.parse(site)
        
                    doc = Document(quad[0], quad[1], quad[2], quad[3], headers, data)
                    documents.append(doc)
                    self._follow(doc, parser, queue, parsed, quad)
                    
    def _follow(self, doc, parser, queue, parsed, quad):
        for elem in doc.get_elements("a"):
            try:
                url = elem['href']
                typ = parser.get_type(url)
                if url in queue:
                    self.logger.info("Url: {0} is in enqueued".format(url))
                elif url in parsed:
                    self.logger.info("Url: {0} was parsed".format(url))
                else:
                    if typ == 'global':
                        queue.append(url)
                    elif typ == 'relative':
                        queue.append(parser.join((quad[0], quad[1], quad[2], url)))
                    elif typ == 'local':
                        if not (url.startswith("javascript:") or url.startswith("?")):
                            queue.append(parser.join((quad[0], quad[1], quad[2], quad[3]+url)))
                        else:
                            self.logger.debug("Omitting: {0} with type {1}".format(url, typ))
            except:
                self.logger.warning("Cannot find href attribute in link: {0}".format(elem))
        