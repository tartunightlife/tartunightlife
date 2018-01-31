#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
usage: server.py [-h] [-v] [-l LADDR] [-p PORT] [-d DUMP] [-m MAX_FILESIZE]

File exchange by Bruno Produit, version 1.0

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -l LADDR, --laddr LADDR
                        Listen address. Default localhost.
  -p PORT, --port PORT  Listen on port.
  -d DUMP, --dump DUMP  Folder as dump dir.
  -m MAX_FILESIZE, --max-filesize MAX_FILESIZE
                        Max filesize for server

"""
import os
import threading
import logging
from constants import *
from argparse import ArgumentParser
import psycopg2
import facebook

# Please use LOGGING
FORMAT = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
LOG = logging.getLogger()

# Connect to DB
#database = open('.pgpass', 'r').read().split(':')
#conn = psycopg2.connect(host=database[0], port=database[1], dbname=database[2], user=database[3], password=database[4])
#pg = conn.cursor()

# Init Facebook Graph API
token = open('.facebook', 'r').read()
fb = facebook.GraphAPI(token)

def info(): return '%s by %s, version %s' % (NAME, AUTHOR, VERSION)

class FacebookScraper:
    def __init__(self):
        LOG.info("Facebook thread started.")

    def get_events(self):
        events = []
        moku = fb.get_object(id=MOKU, fields='events')
        genialistide = fb.get_object(id=GENIALISTIDE, fields='events')
        zavood = fb.get_object(id=ZAVOOD, fields='events')
        illusion = fb.get_object(id=ILLUSION, fields='events')
        shooters = fb.get_object(id=SHOOTERS, fields='events')
        events.append(moku)
        events.append(genialistide)
        events.append(zavood)
        events.append(illusion)
        events.append(shooters)
        return events

        #self.server_thread = threading.Thread(target=self.server.serve_forever)
        #self.server_thread.start()
        #self.server_thread.join()

if __name__=="__main__":
    parser = ArgumentParser(description=info())
    parser.add_argument('-l', '--laddr', help="Listen address. Default localhost.",  default=SERVER_INET_ADDR)
    parser.add_argument('-p', '--port', help="Listen on port.", default=SERVER_PORT, type=int)
    args = parser.parse_args()

    try:
        face = FacebookScraper()
        events = face.get_events()
        print (events)

    except KeyboardInterrupt as e:
        print ('Ctrl+C issued ...')
        print ('Terminating ...')
        sys.exit(0)
