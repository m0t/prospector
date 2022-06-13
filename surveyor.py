#!/usr/bin/env python3

from googlesearch import search
import fileinput
import optparse
import sys

def do_query(word, filetype):
  return search(f"{word} ext:{filetype}", num_results=200)

def parse_args(args):
    parser = optparse.OptionParser("%prog [-t] 'SEARCH TERMS'")
    parser.add_option("-t", "--filetype", help="File type e.g. [DOC, PDF,...]",
                     default="DOC")
    parser.add_option("-Q", "--query", help="query words", default=None)

    opts, args = parser.parse_args(args)

    return opts, args

def main(args):
    opts, args = parse_args(args)

    if opts.query is not None:
        queries = [opts.query]
    else:
        queries = fileinput.input(args[1:])

    for query in queries:
        for url in do_query(query, opts.filetype):
            print(url)

    return 0

if __name__ == "__main__":

    sys.exit(main(sys.argv))
