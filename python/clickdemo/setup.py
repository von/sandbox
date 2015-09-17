#!/usr/bin/env python
# encoding: utf-8

# setuptools is a more powerful version of distutils
try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='clickdemo',
      version='1.0',
      description="Example of click framework",
      author="Von Welch",
      author_email="von@vwelch.com",
      url="http://click.pocoo.org/4/",
      install_requires=[
          'Click',
      ],
      # Modules to install in site-packages
      py_modules=['clickdemo'],
      # Create runnable commands
      entry_points={
          'console_scripts': [
              'clickdemo = clickdemo:cli',
          ],
      },
      )
