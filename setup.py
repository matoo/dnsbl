# -*- coding: utf-8 -*-

import codecs
import os
import re
import sys
from setuptools import setup


def read(*parts):
  filepath = os.path.join(basedir, *parts)
  f = codecs.open(filepath, 'r')
  t = f.read()
  f.close()
  return t

def find_version(*file_paths):
  basedir = os.path.abspath(os.path.dirname(__file__))
  filepath = os.path.join(basedir, *file_paths)
  f = codecs.open(filepath, 'r')
  text = f.read()
  f.close()
  version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                            text, re.M)
  if version_match:
    return version_match.group(1)
  raise RuntimeError("Unable to find version string.")

setup(name = 'dnsbl',
      version = find_version('dnsbl', '__init__.py'),
      description = 'Check IP whether it has been listed on some blacklists or not',
      author = 'amochan',
      author_email = 'amochanyade@gmail.com',
      url = 'https://github.com/matoo/dnsbl',
      license = 'None',
      packages = ['dnsbl'],
      zip_safe = False,
      entry_points = {'console_scripts':['dnsbl_test=dnsbl:main']})
