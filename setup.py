#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
 
setup(name='nfoview',
      version='0.1',
      description='NFOView',
      author='d-fens',
      url='http://github.com/d-fens/nfoview/',
      license = 'MIT',
      scripts=['scripts/nfoview'],
      classifiers=[
            'Environment :: Console',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python'
      ])
