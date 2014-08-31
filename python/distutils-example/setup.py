#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='distutils-example',
      version='1.0',
      description="Example of a distutils-enabled package",
      author="Von Welch",
      author_email="von@vwelch.com",
      url="https://github.com/von/sandbox",
      # Modules to install in site-packages
      py_modules=['distutils-example'],
      # Packages to install in site-packages
      packages=['distutils-package'],
      # Data to be installed with package in site-packages.
      package_data={'distutils-package': ['data/*.txt']},
      # Install scripts. Will be install in bin/
      scripts=['script.py'],
      # Extra data files (install_dir relative to sys prefix, files)
      data_files=[('data', ['data/extra.txt'])],
      )
