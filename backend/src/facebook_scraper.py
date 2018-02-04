#!/usr/bin/python3
# -*- coding: utf-8 -*-

import facebook
import requests
from constants import *
from place import *
from event import *

# TODO better data structures for DB, parsing and fetching
class FacebookScraper:
    def __init__(self):
        # Init Facebook Graph API
        client = open('../misc/facebook', 'r').read().strip().split(':')
        payload = {'client_id': client[0], 'client_secret': client[1], 'grant_type' : 'client_credentials'}
        token = requests.get("https://graph.facebook.com/oauth/access_token", params=payload)
        token = token.json()['access_token']
        self.fb = facebook.GraphAPI(token)

    def fetch_events(self, events):
        parsed = []
        for j in [self.fb.get_object(id=i[0], fields='events') for i in events]:
            for k in j['events']['data']:
                parsed.append(Event(k))
        return parsed


    def fetch_places(self, facebook_ids):
        return [Place(self.fb.get_object(id=i, fields='id,name,website,location'))
                for i in facebook_ids]
