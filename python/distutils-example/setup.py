#!/usr/bin/env python
# encoding: utf-8

# setuptools is a more powerful version of distutils
try:
    from setuptools import setup
except:
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
      # Create runnable commands
      entry_points={
          'console_scripts': [
              'disutils_example = disutils_module:main',
          ],
      },
      # Extra data files (install_dir relative to sys prefix, files)
      data_files=[('data', ['data/extra.txt'])],
      )
