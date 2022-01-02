import os

import appdirs

# How many samples of the word list for the final password?
N = 4
# How to join each word
SEPARATOR = '-'
# Maximum number of chars. in each word
MAX_LEN = 10
# Minimum number of bits of entropy required
MIN_ENTROPY = 40

# cross-platform word list locations
# (can be adjusted, depening on desired vocab.)
SYSTEM_WORD_LISTS = [
    '/usr/share/dict/british-english', '/usr/share/dict/words',
    '/usr/share/dict/web2'
]

# network locations for remote word list (zip archive expected)
REMOTE_WORD_LIST = ('https://sourceforge.net/'
                    'projects/wordlist/files/speller/2020.12.07/'
                    'wordlist-en_GB-large-2020.12.07.zip/download')

# cross-platform cache directory location
CACHE_DIR = appdirs.user_cache_dir('mempw', 'mdvthu')
WORD_LIST_FN = 'wordlist.txt'
CACHED_WORD_LIST = os.path.join(CACHE_DIR, WORD_LIST_FN)
