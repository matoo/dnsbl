# -*- coding: utf-8 -*-

import socket


def hostname_exist(hostname):
  if not isinstance(hostname, (str, unicode)):
    return False
  elif _validate_IPv4_format(hostname):
    return False
  elif _validate_IPv6_format(hostname):
    return False
  try:
    addrinfo = socket.getaddrinfo(hostname, None)
  except socket.gaierror:
    return False
  return True

def domain_name_pointer(ip):
  if not isinstance(ip, (str, unicode)):
    return ''
  if _validate_IPv4_format(ip):
    return _domain_name_pointer_ipv4(ip)
  elif _validate_IPv6_format(ip):
    return _domain_name_pointer_ipv6(ip)
  else:
    return ''

def _domain_name_pointer_ipv4(ipv4):
  if not _validate_IPv4_format(ipv4):
    return ''
  ipv4_list = socket.inet_pton(socket.AF_INET, ipv4)
  reverse_ipv4 = socket.inet_ntop(socket.AF_INET, ipv4_list[::-1])
  return reverse_ipv4 + '.in-addr.arpa'

def _domain_name_pointer_ipv6(ipv6):
  if not _validate_IPv6_format(ipv6):
    return ''
  ipv6_hex = socket.inet_pton(socket.AF_INET6, ipv6).encode('hex')
  reverse_ipv6_hex = ipv6_hex[::-1]
  return '.'.join(reverse_ipv6_hex) + '.ip6.arpa'

def _validate_IPv4_format(ipv4):
  try:
    socket.inet_pton(socket.AF_INET, ipv4)
  except socket.error:
    return False
  return True

def _validate_IPv6_format(ipv6):
  try:
    socket.inet_pton(socket.AF_INET6, ipv6)
  except socket.error:
    return False
  return True
