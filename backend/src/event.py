#!/usr/bin/python3
# -*- coding: utf-8 -*-

from constants import *

class Event:
    def __init__(self, dictionary):
        if 'start_time' in dictionary:
            self.time = dictionary['start_time']
        self.name = dictionary['name']
        self.id = dictionary['id']
        if 'place' in dictionary:
            self.address = dictionary['place']['location']['street'] + ', ' +\
                                dictionary['place']['location']['city'] + ', ' +\
                                dictionary['place']['location']['country']
    def insert(pg, table, data):
        return pg.query("INSERT INTO " + table + " VALUES ('" + \
                       data.id + "', '" + data.name + "', '" + data.address + "', '" + data.time + \
                        "') ON CONFLICT DO NOTHING;")

    def select(pg, columns, table, where="TRUE"):
        return pg.query("SELECT " + columns + " FROM " + table + " WHERE " + where + ";")
