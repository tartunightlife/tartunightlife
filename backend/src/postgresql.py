#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
from constants import *

# TODO prepared query for security
# This works but it is just a test
class PostgreSQL:

    def __init__(self):
        # Init DB connection
        pgpass = open('../misc/pgpass', 'r').read().split(':')
        self.conn = psycopg2.connect("dbname=" + pgpass[2] + " user=" + pgpass[3]\
                                + " password=" + pgpass[4] + " port="+ pgpass[1])
        self.cur = self.conn.cursor()
        self.conn.autocommit=True

    def query(self, query):
        self.cur.execute(query)
        res = None
        try:
            res = self.cur.fetchall()
        except psycopg2.ProgrammingError:
            print("nothing to fetch")
        return res
