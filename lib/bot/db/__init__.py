# -*- coding: utf-8 -*-

import psycopg2
import logging

from bot.document import Document

class BotDB:
    
    FIND_SITE = "SELECT * FROM sites WHERE domain=%s AND protocol=%s AND secure=%s"
    
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Connecting to database, host: {0}".format(config['db']['host']))
        
        try:
            self.connection = psycopg2.connect(database=config['db']['name'], 
                                               user=config['db']['user'], 
                                               password=config['db']['pass'], 
                                               host=config['db']['host'],
                                               port=config['db']['port'])
            self.cursor = self.connection.cursor()
        
        except psycopg2.Error, e:
            self.logger.fatal("Cannot connect to database...")
            self.logger.fatal("...check connection settings")
            self.logger.fatal(str(e))
            raise Exception("Database connection error!")
        
        self.logger.info("Connected successfully")
    
    def find_document(self, site, location):
        pass
    
    def find_site(self, domain, protocol, secure=False):
        result = self.cursor.execute(self.FIND_SITE, domain, protocol, secure)
        
        
    def add_document(self, document):
        pass