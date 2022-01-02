'''
Wordlist management

Internet downloaded word lists are useful if there is insufficient entropy
from the installed lists (for example, on Windows)
'''

import logging
import os
import shutil
import sys
import tempfile

import requests

from . import config


def _create_cache(dir_path=config.CACHE_DIR):
    '''
    If the cache directory doesn't exist, create it
    '''
    if os.path.isdir(dir_path):
        logging.info("Directory ({}) exists".format(dir_path))
    else:
        logging.info("Directory not found, creating {}".format(dir_path))
        os.mkdir(dir_path)


def _download():
    '''
    Download and extract the word list zip to a temp location
    Move the largest non-zip file to the cache
    '''
    zipped_list = requests.get(config.REMOTE_WORD_LIST).content
    with tempfile.TemporaryDirectory() as td:
        zip_tmp_location = os.path.join(td, 'download.zip')
        with open(zip_tmp_location, 'bw') as f:
            f.write(zipped_list)
        shutil.unpack_archive(zip_tmp_location, td)
        unzipped = [(f, os.stat(os.path.join(td, f)).st_size)
                    for f in os.listdir(td) if not f.endswith('.zip')]
        largest_unzipped = sorted(unzipped, key=lambda x: x[1])[-1]
        os.rename(os.path.join(td, largest_unzipped[0]),
                  config.CACHED_WORD_LIST)
    logging.info('Downladed {} as {} ({} bytes)'.format(
        largest_unzipped[0], config.WORD_LIST_FN, largest_unzipped[1]))


def _load():
    '''
    Load the word list file from the cache
    '''
    with open(config.CACHED_WORD_LIST, 'rt') as f:
        wordlist = f.readlines()
    # remove trailing newlines (\n)
    return [w.strip() for w in wordlist if w]


def words():
    '''
    Get a resonable list of words
    '''
    if not os.path.isfile(config.CACHED_WORD_LIST):
        _create_cache()
        _download()
    # check that at least one wordlist is accessible
    WORD_LISTS = [
        fn for fn in config.SYSTEM_WORD_LISTS + [config.CACHED_WORD_LIST]
        if os.path.isfile(fn)
    ]
    if len(WORD_LISTS) == 0:
        logging.error("Unable to load any wordlists: "
                      "ensure ispell dictionary is installed")
        sys.exit(-1)
    return set(_load())
