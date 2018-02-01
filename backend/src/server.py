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
from postgresql import *
from argparse import ArgumentParser
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
    pg = PostgreSQL()

    # Facebook
    fb = FacebookScraper()

    return pg, fb

def info(): return '%s by %s, version %s' % (NAME, AUTHOR, VERSION)

def parse_facebook_places(place):
    return places

def parse_facebook_events(events):
    parsed = []
    for i in events:
        for j in i['events']['data']:
            evnt = {}
            evnt['name'] = j['name']
            evnt['uuid'] = j['id']
            evnt['address'] = j['place']['location']['street'] + ', ' +\
                                j['place']['location']['city'] + ', ' +\
                                j['place']['location']['country']
            parsed.append(evnt)
    return parsed

#-------------- Main -------------------------

if __name__=="__main__":
    try:
        # Init
        pg, fb = initialize()

        # Facebook Scraping
        events = fb.get_events()

        events = parse_facebook_events(events)

        for i in events:
            pg.insert("places", i)

        print(pg.select("*", "places"))


        # REST Service
        app = Eve()
        app.run()

    except KeyboardInterrupt as e:
        print ('Ctrl+C issued ...')
        print ('Terminating ...')
        sys.exit(0)
