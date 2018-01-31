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
import os
import threading
import logging
from constants import *
from argparse import ArgumentParser
import psycopg2
import facebook
import requests
# Please use LOGGING
FORMAT = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
LOG = logging.getLogger()

def initialize():
    # Connect to DB
    database = open('.pgpass', 'r').read().split(':')
    #conn = psycopg2.connect(host=database[0], port=int(database[1]), database=database[2], user=database[3], password=database[4])
    #pg = conn.cursor()

    # Init Facebook Graph API
    client = open('.facebook', 'r').read().strip().split(':')
    payload = {'client_id': client[0], 'client_secret': client[1], 'grant_type' : 'client_credentials'}
    token = requests.get("https://graph.facebook.com/oauth/access_token", params=payload)
    token = token.json()['access_token']
    fb = facebook.GraphAPI(token)

def info(): return '%s by %s, version %s' % (NAME, AUTHOR, VERSION)

class FacebookScraper:
    def __init__(self):
        LOG.info("Facebook thread started.")

    def get_events(self):
        events = []
        for i in PLACES:
            events.append(fb.get_object(id=i, fields='events'))
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
        initialize()
        face = FacebookScraper()
        events = face.get_events()
        print (events)


    except KeyboardInterrupt as e:
        print ('Ctrl+C issued ...')
        print ('Terminating ...')
        sys.exit(0)
