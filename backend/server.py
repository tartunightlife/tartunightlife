#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
usage: server.py [-h] [-v] [-l LADDR] [-p PORT] [-d DUMP] [-m MAX_FILESIZE]

File exchange by Bruno Produit, version 1.0

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -l LADDR, --laddr LADDR
                        Listen address. Default localhost.
  -p PORT, --port PORT  Listen on port.
  -d DUMP, --dump DUMP  Folder as dump dir.
  -m MAX_FILESIZE, --max-filesize MAX_FILESIZE
                        Max filesize for server

"""
import os
import threading
import logging
from constants import *
from argparse import ArgumentParser
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Please use LOGGING
FORMAT = '%(asctime)-15s %(levelname)s %(threadName)s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
LOG = logging.getLogger()

def info(): return '%s by %s, version %s' % (NAME, AUTHOR, VERSION)



class Server:
    def __init__(self, args):
        LOG.info("Server Started.")
        self.directory = args.dump
        # Initilize RPC service on specific port
        self.server = SimpleXMLRPCServer((args.laddr, args.port))
        LOG.debug( "Listening on port " + str(args.port) + "...")
        # Register server-side functions into RPC middleware
        self.server.register_function(self.upload, "upload")
        self.server.register_function(self.download, "download")
        self.server.register_function(self.ls, "ls")
        self.server.register_function(self.delete, "delete")
        self.server.register_function(self.move, "move")
        # Start the main thread now
        # start the RPC server
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()
        self.server_thread.join()
    def upload(self, filename, data):
        filelength = len(data)
        size = os.statvfs(self.directory)
        free = size.f_bsize * size.f_bavail

        if filelength > free:
            LOG.debug( 'No enough space left. Closing client socket')
            return NO_SPACE
        elif os.path.exists(self.directory+ "/" + filename):
            LOG.debug( 'File already exist, not writing. Closing client socket')
            return FILENAME_TAKEN
        else:
            f = open(self.directory + "/" + filename,'wb') #open in binary
            f.write(data)
            f.close()
            LOG.debug( "received file was written to " + self.directory + "/" + filename)
            return ACK

    def download(self, filename):
        LOG.debug( filename)
        if os.path.exists(filename):
            f = open(filename, 'rb')
            data = f.read()
            return ACK, data
        else:
            LOG.debug( 'File does not exist, no download possible')
            return FILE_DOESNT_EXIST, _

    def ls(self):
        return os.listdir(self.directory)

    def move(self, oldfile, newfile):
        os.rename(oldfile, newfile)
        return ACK
    def delete(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
            return ACK
        else:
            return FILE_DOESNT_EXIST


if __name__=="__main__":
    parser = ArgumentParser(description=info(), version = VERSION)
    parser.add_argument('-l', '--laddr', help="Listen address. Default localhost.",  default=SERVER_INET_ADDR)
    parser.add_argument('-p', '--port', help="Listen on port.", default=SERVER_PORT, type=int)
    parser.add_argument('-d', '--dump', help="Folder as dump dir.", default="dump")
    parser.add_argument('-m', '--max-filesize', help="Max filesize for server", default=10*1024*1024, type=int)
    args = parser.parse_args()
    if not os.path.exists(args.dump):
        os.mkdir(args.dump)
    try:
        s = Server(args)
    except KeyboardInterrupt as e:
        print 'Ctrl+C issued ...'
        print 'Terminating ...'
        sys.exit(0)
