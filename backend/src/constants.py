#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

# Logging
FORMAT = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
LOGFILE = '../log/server.log'
logging.basicConfig(filename=LOGFILE, filemode='a',level=logging.DEBUG, format=FORMAT)
LOG = logging.getLogger()

# Information about the program
NAME = 'Tartu Night Life Backend' # Name of the app
AUTHOR = 'Bruno Produit, Basar Turgut, Abel Mesfin, Saumitra Bagchi' # List of authors
VERSION = '0.1' # Version, constant must be changed at each new milestone

# IP:Port
SERVER_INET_ADDR = '127.0.0.1' # IP to listen to
SERVER_PORT = 1234 # Port to listen to

# FB links
DEFAULT_TARTU_PLACES = ['mokubaar', 'GenKlubi', 'klubi.illusion', 'shooterstartu', 'lokaalarhiiv'] # To be replaced by Places in DB
