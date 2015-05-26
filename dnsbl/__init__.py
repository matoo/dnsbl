# -*- coding: utf-8 -*-

from optparse import OptionParser
import sys

import dnsbl.host


__version__ = '0.0.2'
_usage = 'dnsbl.py [-h|--help] [--version] ip_address'
_blacklist_host = [
  'b.barracudacentral.org',
  'zen.spamhaus.org',
  'bl.spamcop.net',
  'all.spamrats.com'
]


def main(args=None):
  parser = OptionParser(usage=_usage, version=__version__)
  (options, args) = parser.parse_args()

  if len(args) != 1:
    parser.print_usage()

  PTR = host.domain_name_pointer(args[0])
  if len(PTR) == 0:
    parser.print_usage()
  reverse_ip = PTR.rsplit('.', 2)[0]
  print('DNSBL check for %s' % args[0])
  for b in _blacklist_host:
    h = reverse_ip + '.' + b
    result = 'Listed' if host.hostname_exist(h) else 'Not Listed'
    print('%-30s %s' % (b, result))


if __name__ == '__main__':
  sys.exit(main())
