# -*- coding: utf-8 -*-

from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'GracefulKiller',
  packages = ['GracefulKiller'],
  version = '0.2',
  license = 'MIT',
  description = "module for process SIGTERM, SIGHUP and SIGINT signals gracefully",
  author = 'Maxim Toropov',
  author_email = 'maxim.vt@gmail.com',
  url = 'https://github.com/MaxMaxoff/GracefulKiller',
  download_url = 'https://github.com/MaxMaxoff/GracefulKiller/archive/v_02.tar.gz',
  keywords = ['SIGTERM', 'SIGINT', 'SIGHUP', 'GracefulKiller', 'Killer', 'Graceful'],
  install_requires = [
      ],
  classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable      
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ]
)