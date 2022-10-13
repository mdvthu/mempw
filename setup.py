from setuptools import setup

setup(name='mempw',
      version='0.1.6',
      description='Python-based memorable password generator',
      long_description=('Generates pronouncable passwords '
                        'based on system wordlists'),
      long_description_content_type='text/x-rst',
      author='Mark Thurston',
      author_email='mark@mdvthu.com',
      url='https://github.com/mdvthu/mempw',
      license='Apache Licence version 2',
      license_files=('LICENCE'),
      packages=['mempw'],
      install_requires=['appdirs', 'requests'],
      entry_points={'console_scripts': ['mempw=mempw.core:cli']})
