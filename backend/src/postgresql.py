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

    def insert(self, table, values):
        self.cur.execute("INSERT INTO " + table + """ VALUES (%s, %s, %s, %s)\
        ON CONFLICT DO NOTHING;""",\
                  (values['uuid'], values['name'], values['address'], ''))

    def select(self, columns, table, where="TRUE"):
        self.cur.execute("SELECT " + columns + " FROM " + table + " WHERE " + where + ";")
        return self.cur.fetchall()
