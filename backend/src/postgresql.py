#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
from constants import *

# TODO prepared query for security
# This works but it is just a test
class PostgreSQL:

    def __init__(self):
        """
        Register psycopg2 to talk to the PostgreSQL database
        with the given constants in constants.py
        """

        # Init DB connection
        LOG.info("Initializing PostgreSQL connection...")
        pgpass = open('../misc/pgpass', 'r').read().split(':')
        self.conn = psycopg2.connect("dbname=" + pgpass[2] + " user=" + pgpass[3]\
                                + " password=" + pgpass[4] + " port="+ pgpass[1])
        self.cur = self.conn.cursor()

        # In order to commit directly, we autocommit to the DB.
        # Unoptimized but good enough for our usage.
        self.conn.autocommit=True

    def query(self, query):
        """
        Generic single query handling for PostgreSQL.
        It executes the query directly without waiting for the pool.
        returns the result in a string if there is any, else it returns None
        """

        LOG.info(query)
        self.cur.execute(query)
        res = None
        try:
            res = self.cur.fetchall()
        except psycopg2.ProgrammingError:
            LOG.debug("nothing to fetch")
        return res
