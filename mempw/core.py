#!/usr/bin/env python3
'''Python based pronouncable password generator'''
import logging
import os
import random
import sys

from . import config

# check that at least one wordlist is accessible
WORD_LISTS = [fn for fn in config.WORD_LISTS if os.path.isfile(fn)]
if len(WORD_LISTS) == 0:
    logging.error(
        "Unable to load any wordlists: ensure ispell dictionary is installed")
    sys.exit(-1)

# create a long list of all the words existing in the files
words = list()
for fn in WORD_LISTS:
    with open(fn, 'rt') as f:
        words.extend(f.readlines())


def process(word):
    '''
    Remove newlines and apostrophes
    Title case each word
    Exclude words longer than the preferred length
    '''
    word = word.replace('\n', '')
    word = word.replace("'", '')
    word = word.title()
    if len(word) <= config.MAX_LEN:
        return word
    else:
        return None


# pre-process all the loaded words
words = [process(word) for word in words if process(word) is not None]


def new_password(seed=None):
    if seed:
        random.seed(seed)
    return config.SEPARATOR.join(random.choices(words, k=config.N))
