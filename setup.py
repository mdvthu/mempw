from setuptools import setup

setup(name='mempw',
      version='0.1.4',
      description='Python-based memorable password generator',
      long_description=('Generates pronouncable passwords '
                        'based on system wordlists'),
      author='Mark Thurston',
      author_email='mark@mdvthu.com',
      url='https://github.com/mdvthu/mempw',
      license_files=('LICENCE'),
      packages=['mempw'],
      install_requires=['appdirs'],
      entry_points={'console_scripts': ['mempw=mempw.core:cli']})
