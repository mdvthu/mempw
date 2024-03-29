#!/usr/bin/env python3
'''Python based pronouncable password generator'''
import logging
import math
import random
import sys

from . import config, wordlist


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


# create a long list of all the words existing in the files
words = wordlist.words()
# pre-process all the loaded words
words = [process(word) for word in words if process(word) is not None]
possible_combinations = len(words)**config.N
if math.log(possible_combinations, 2) < config.MIN_ENTROPY:
    logging.error("Wordlist length not enough to create desired entropy")
    sys.exit(1)


def new_password(seed=None):
    if seed:
        random.seed(seed)
    return config.SEPARATOR.join(random.choices(words, k=config.N))


def cli():
    ''' Windows-compatible command line interface '''
    print(new_password())
