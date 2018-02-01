#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
usage: server.py [-h] [-l LADDR] [-p PORT]

Tartu Night Life by Bruno Produit, Basar Turgut, Abel Mesfin, Saumitra Bagchi,
version 1.0

optional arguments:
  -h, --help            show this help message and exit
  -l LADDR, --laddr LADDR
                        Listen address. Default localhost.
  -p PORT, --port PORT  Listen on port.
"""

#-------------- Imports -------------------------

import logging
from constants import *
from facebook_scraper import *
from argparse import ArgumentParser
import psycopg2
from eve import Eve

#-------------- Methods -------------------------

def initialize():
    # Logging
    FORMAT = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    LOG = logging.getLogger()

    # Arguments
    parser = ArgumentParser(description=info())
    parser.add_argument('-l', '--laddr', help="Listen address. Default localhost.",  default=SERVER_INET_ADDR)
    parser.add_argument('-p', '--port', help="Listen on port.", default=SERVER_PORT, type=int)
    args = parser.parse_args()

    # Database
    database = open('.pgpass', 'r').read().split(':')
    #conn = psycopg2.connect(host=database[0], port=int(database[1]), database=database[2], user=database[3], password=database[4])
    #pg = conn.cursor()

def info(): return '%s by %s, version %s' % (NAME, AUTHOR, VERSION)


#-------------- Main -------------------------

if __name__=="__main__":
    try:
        # Init
        initialize()

        # Facebook Scraping
        fb = FacebookScraper()
        events = fb.get_events()
        print (events)
        app = Eve()
        app.run()

    except KeyboardInterrupt as e:
        print ('Ctrl+C issued ...')
        print ('Terminating ...')
        sys.exit(0)
