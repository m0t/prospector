<<<<<<< HEAD
#!/usr/bin/env python3

from googlesearch import search
=======
#!/usr/bin/env python

from pybing.query import WebQuery
from urlparse import urlparse,parse_qs
>>>>>>> 1c29c33f181f9efa3a8a9dab3a9a9b3d9e1f31d5
import fileinput
import optparse
import sys

<<<<<<< HEAD
def do_query(word, filetype):
  return search(f"{word} ext:{filetype}", num_results=200)

def parse_args(args):
    parser = optparse.OptionParser("%prog [-t] 'SEARCH TERMS'")
    parser.add_option("-t", "--filetype", help="File type e.g. [DOC, PDF,...]",
                     default="DOC")
=======
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
>>>>>>> 1c29c33f181f9efa3a8a9dab3a9a9b3d9e1f31d5
    parser.add_option("-Q", "--query", help="query words", default=None)

    opts, args = parser.parse_args(args)

    return opts, args

def main(args):
    opts, args = parse_args(args)

<<<<<<< HEAD
=======
    global keyfile

>>>>>>> 1c29c33f181f9efa3a8a9dab3a9a9b3d9e1f31d5
    if opts.query is not None:
        queries = [opts.query]
    else:
        queries = fileinput.input(args[1:])

<<<<<<< HEAD
    for query in queries:
        for url in do_query(query, opts.filetype):
            print(url)
=======
    if opts.key is None:
      key = read_key(keyfile)
    else:
      key = opts.key

    for query in queries:
        #for url in do_query(query, opts.filetype, key):
        for url in do_query(query, key):
            print url
>>>>>>> 1c29c33f181f9efa3a8a9dab3a9a9b3d9e1f31d5

    return 0

if __name__ == "__main__":

    sys.exit(main(sys.argv))
