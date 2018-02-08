#!/usr/bin/python3
# -*- coding: utf-8 -*-

import facebook
import requests
from constants import *
from place import *
from event import *

# TODO better data structures for DB, parsing and fetching
class FacebookScraper:
    """ This object represents the scraper used to get events and places on Facebook. """

    def __init__(self):
        """ Initializing the Facebook middleware and log in to scrape """

        # Init Facebook Graph API
        LOG.info("Initializing Facebook Graph API...")
        client = open('../misc/facebook', 'r').read().strip().split(':')
        payload = {'client_id': client[0], 'client_secret': client[1], 'grant_type' : 'client_credentials'}
        token = requests.get("https://graph.facebook.com/oauth/access_token", params=payload)
        token = token.json()['access_token']
        self.fb = facebook.GraphAPI(token)

    def fetch_events(self, places):
        """ Returns a list of dictionaries representing the upcoming events of the given places """

        LOG.info("FB fetch events...")
        parsed = []
        for j in [self.fb.get_object(id=i[0], fields='events') for i in places]:
            for k in j['events']['data']:
                parsed.append(Event(k))
        return parsed


    def fetch_places(self, facebook_ids):
        """ Returns a list of dictionaries representing the places given by the facebook_ids """

        LOG.info("FB fetch places...")
        return [Place(self.fb.get_object(id=i, fields='id,name,website,location'))
                for i in facebook_ids]
