#edit-mode: -*- python -*-
#coding:utf8

'''
A HTTP server to search 
'''
import sys
sys.path.append('../pylib')

import tornado.ioloop
import tornado.web
import json
import traceback
import thread
import time
import socket
import os
from threading import Thread
import logging
import cPickle as pickle

logging.basicConfig(filename='info.log', level=logging.DEBUG, filemode='w',
    format='[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)s] %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')

CACHE_FILE = './.cache.dat'
cache = {}

if os.path.exists(CACHE_FILE):
    fin = open(CACHE_FILE, 'r')
    cache = pickle.load(fin)
    fin.close()

def handle_request(args):
    action = args.get('action')
    if not action:
        cache[args['key']] = args['value']
    if action == 'dump':
        fout = open(CACHE_FILE, 'w')
        pickle.dump(cache, fout)
        fout.close()

class StaticHandler(tornado.web.RequestHandler):
    def set_extra_headers(self, path):  
        self.set_header("Cache-control", "no-cache")

class BasicHandler(tornado.web.RequestHandler):
    def get(self):
        args = {}
        for k, v in self.request.arguments.iteritems():
            args[k] = v[0]
        logging.info('recieve >%s<' % str(args))
        result = {'errno' : 0, 'errmsg' : ''}
        try:
            result['data'] = handle_request(args) or {}
            result_str = json.dumps(result)
        except:
            msg = traceback.format_exc()
            logging.error(msg)
            result_str = '{"errno":1, "errmsg":"%s"}' % msg
        logging.info("response >%s<" % result_str)
        self.write(result_str)

def http_server(port):
    application = tornado.web.Application([
        (r"/api", BasicHandler),
        (r"/static/(.*)", StaticHandler,)], 
        static_path = "/Users/liyong/leon/github/trading_area/static"
    )
    application.listen(port)
    logging.info('http server serving...')
    tornado.ioloop.IOLoop.instance().start()
    logging.info('http server exit')

if __name__ == "__main__":
    # 因为UNIX Socket相比HTTP似乎也没有性能优势，所以直接就全部HTTP吧。这样还能避免共享资源加锁。
    # start_servers()
    http_server(8888)

