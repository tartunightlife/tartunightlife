#!/usr/bin/python3
# -*- coding: utf-8 -*-

from constants import *

class Place:
    def __init__(self, dictionary):
        if 'website' in dictionary:
            self.website = dictionary['website']
        self.name = dictionary['name']
        self.id = dictionary['id']
        if 'location' in dictionary:
            self.address = dictionary['location']['street'] + ', ' +\
                                dictionary['location']['city'] + ', ' +\
                                dictionary['location']['country']

    def insert(pg, table, data):
        if hasattr(data, 'website'):
            website = data.website
        else:
            website = ''
        return pg.query("INSERT INTO " + table + " VALUES ('" + \
                       data.id + "', '" + data.name + "', '" + data.address + "', '" + website + \
                        "') ON CONFLICT DO NOTHING;")

    def select(pg, columns, table, where="TRUE"):
        return pg.query("SELECT " + columns + " FROM " + table + " WHERE " + where + ";")
