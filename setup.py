#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import os

reqs = [
'mock',
'coveralls',
'sphinx',
'mako',
'pyramid',
'pyramid_mako',
'waitress',
'pandas',
]

try:
   import pypandoc
   README = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   README = ''

setup(name='cogfusion',
      version='0.0',
      author='Daniel Kessler, Cogfusion Authors',
      author_email='kesslerd@umich.edu',
      description='...',
      packages=find_packages(),
      url = 'https://github.com/dankessler/cogfusion',
      test_suite="tests",
      zip_safe=False,
      license='MIT',
      long_description=README,
      entry_points="""\
[paste.app_factory]
main = cogfusion:main
""",
      classifiers=[
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering'],
      install_requires=reqs,
      include_package_data=True,
      scripts=['exe/cogfusion'],
      )
