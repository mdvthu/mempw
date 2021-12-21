# -*- coding: utf-8 -*-

from setuptools import setup

with open('LICENCE') as f:
    licence = f.read()

setup(name='mempw',
      version='0.1.0',
      description='Python-based memorable password generator',
      long_description=('Generates pronouncable passwords '
                        'based on system wordlists'),
      author='Mark Thurston',
      author_email='mark@mdvthu.com',
      url='https://github.com/mdvthu/mempw',
      license=licence,
      packages=['mempw'],
      scripts=['scripts/mempw'])
