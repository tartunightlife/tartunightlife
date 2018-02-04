#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
usage: server.py [-h] [-i IP] [-p PORT] [-P PLACES]

Tartu Night Life Backend by Bruno Produit, Basar Turgut, Abel Mesfin, Saumitra
Bagchi, version 0.1

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        Listen address. Default localhost.
  -p PORT, --port PORT  Listen on port.
  -P PLACES, --places PLACES
                        Facebook id of places

"""

#-------------- Imports -------------------------

import logging
from constants import *
from facebook_scraper import *
from postgresql import *
from argparse import ArgumentParser
from eve import Eve
from eve_swagger import swagger, add_documentation
from multiprocessing import Process

#-------------- Methods -------------------------

def initialize():
    # Logging
    FORMAT = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    LOG = logging.getLogger()

    # Arguments
    parser = ArgumentParser(description=info())
    parser.add_argument('-i', '--ip', help="Listen address. Default localhost.",  default=SERVER_INET_ADDR)
    parser.add_argument('-p', '--port', help="Listen on port.", default=SERVER_PORT, type=int)
    parser.add_argument('-P', '--places', help="Facebook id of places",  default=DEFAULT_TARTU_PLACES)
    args = parser.parse_args()

    # Database
    pg = PostgreSQL()

    # Facebook
    fb = FacebookScraper()
    places = fb.fetch_places(args.places)
    for i in places:
        Place.insert(pg, "places", i)

    # REST Service
    app = Eve()
    app.register_blueprint(swagger)
    app.config['SWAGGER_INFO'] = open('../utils/swagger.json', 'r').read()
    app.config['SWAGGER_HOST'] = args.ip
    return pg, fb, app

def info(): return '%s by %s, version %s' % (NAME, AUTHOR, VERSION)


def facebook_process(pg, fb):
    # Facebook Scraping
    events = fb.fetch_events(pg.query("SELECT fb_id FROM places;"))

    for i in events:
        Event.insert(pg, "events", i)
#-------------- Main -------------------------

if __name__=="__main__":
    try:
        # Init
        pg, fb, app = initialize()

        # Register Processes
        processes = []

        processes.append(Process(target=facebook_process, args=(pg, fb)))
        processes.append(Process(target=print(pg.query("SELECT * FROM places;"))))
        processes.append(Process(target=app.run()))

        for i in processes:
            i.start()
            i.join()

    except KeyboardInterrupt as e:
        print ('Ctrl+C issued ...')
        print ('Terminating ...')
        sys.exit(0)
