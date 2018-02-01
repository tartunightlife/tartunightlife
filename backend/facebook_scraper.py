#!/usr/bin/python3
# -*- coding: utf-8 -*-

import facebook
import requests
from constants import *

class FacebookScraper:
    def __init__(self):
        # Init Facebook Graph API
        client = open('.facebook', 'r').read().strip().split(':')
        payload = {'client_id': client[0], 'client_secret': client[1], 'grant_type' : 'client_credentials'}
        token = requests.get("https://graph.facebook.com/oauth/access_token", params=payload)
        token = token.json()['access_token']
        self.fb = facebook.GraphAPI(token)

    def get_events(self):
        events = []
        for i in PLACES:
            events.append(self.fb.get_object(id=i, fields='events'))
        return events
