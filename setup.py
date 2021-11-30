# -*- coding: utf-8 -*-

from setuptools import setup

with open('README') as f:
    readme = f.read()

with open('LICENCE') as f:
    licence = f.read()

setup(name='pypw',
      version='0.1.0',
      description='Python-based password generator',
      long_description=readme,
      author='Mark Thurston',
      author_email='mark@mdvthu.com',
      url='https://github.com/mdvthu/pypw',
      license=licence,
      packages=['pypw'],
      scripts=['scripts/pypw'])
