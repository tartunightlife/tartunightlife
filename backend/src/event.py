#!/usr/bin/python3
# -*- coding: utf-8 -*-

from constants import *

class Event:
    """
    This object represents the 'Event' object in the database.
    It is used instead of a simple dictionary in order to be able
    to link it with the parsing of the scraper and with its specific SQL queries.
    It is also used for clarity, each column is a parameter of the object,
    e.g 'thisparty.name', 'thatparty.start_time'.
    """

    def __init__(self, dictionary):
        """ Initializing the 'place' object by parsing the dictionary given by Facebook """

        LOG.info("New Event created")
        if 'start_time' in dictionary:
            self.time = dictionary['start_time']
        self.name = dictionary['name']
        self.id = dictionary['id']
        if 'place' in dictionary:
            self.address = dictionary['place']['location']['street'] + ', ' +\
                                dictionary['place']['location']['city'] + ', ' +\
                                dictionary['place']['location']['country']

    def insert(pg, table, data):
        """ Returns the INSERT SQL query string for the 'Event' object """

        return pg.query("INSERT INTO " + table + " VALUES ('" + \
                       data.id + "', '" + data.name + "', '" + data.address + "', '" + data.time + \
                        "') ON CONFLICT DO NOTHING;")

    def select(pg, columns, table, where="TRUE"):
        """ Returns the SELECT SQL query string for the 'Place' object """

        return pg.query("SELECT " + columns + " FROM " + table + " WHERE " + where + ";")
