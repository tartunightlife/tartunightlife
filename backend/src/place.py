#!/usr/bin/python3
# -*- coding: utf-8 -*-

from constants import *

class Place:
    """
    This object represents the 'Place' object in the database.
    It is used instead of a simple dictionary in order to be able
    to link it with the parsing of the scraper and with its specific SQL queries.
    It is also used for clarity, each column is a parameter of the object,
    e.g 'nicebar.address', 'thatcoffeeplace.website'.
    """

    def __init__(self, dictionary):
        """ Initializing the 'place' object by parsing the dictionary given by Facebook """

        LOG.info("New Place created")
        if 'website' in dictionary:
            self.website = dictionary['website']
        self.name = dictionary['name']
        self.id = dictionary['id']
        if 'location' in dictionary:
            self.address = dictionary['location']['street'] + ', ' +\
                                dictionary['location']['city'] + ', ' +\
                                dictionary['location']['country']

    def insert(pg, table, data):
        """ Returns the INSERT SQL query string for the 'Place' object """

        if hasattr(data, 'website'):
            website = data.website
        else:
            website = ''
        return pg.query("INSERT INTO " + table + " VALUES ('" + \
                       data.id + "', '" + data.name + "', '" + data.address + "', '" + website + \
                        "') ON CONFLICT DO NOTHING;")

    def select(pg, columns, table, where="TRUE"):
        """ Returns the SELECT SQL query string for the 'Place' object """

        return pg.query("SELECT " + columns + " FROM " + table + " WHERE " + where + ";")
