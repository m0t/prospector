#!/usr/bin/env python

from pybing.query import WebQuery
from urlparse import urlparse,parse_qs
import fileinput
import optparse
import sys

keyfile='key.txt'

def do_query(word, key):

  '''
      try:
          for r in query.execute():
              try:
                  yield r.url.decode('utf-8').encode('utf-8')
              except:
                  pass
      except:
          pass
  '''
  #query = WebQuery(key, word, filetype.upper())
  query = WebQuery(key, word)
  for r in query.execute():
    yield parse_qs(urlparse(r.url.decode('utf-8').encode('utf-8')).query)["r"][0]

def read_key(keyfile):

    f=open(keyfile)
    
    return f.read().strip()

def parse_args(args):
    parser = optparse.OptionParser("%prog [-k] [-t] 'SEARCH TERMS'")
    parser.add_option("-k", "--key", help="Bing API key", default=None)
    #parser.add_option("-t", "--filetype", help="File type e.g. [DOC, PDF,...]", default="DOC")
    parser.add_option("-Q", "--query", help="query words", default=None)

    opts, args = parser.parse_args(args)

    return opts, args

def main(args):
    opts, args = parse_args(args)

    global keyfile

    if opts.query is not None:
        queries = [opts.query]
    else:
        queries = fileinput.input(args[1:])

    if opts.key is None:
      key = read_key(keyfile)
    else:
      key = opts.key

    for query in queries:
        #for url in do_query(query, opts.filetype, key):
        for url in do_query(query, key):
            print url

    return 0

if __name__ == "__main__":

    sys.exit(main(sys.argv))
