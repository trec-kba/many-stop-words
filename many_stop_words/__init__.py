'''many_stop_words has lists of stop words in many languages

.. This software is released under an MIT/X11 open source license.
   Copyright 2012-2014 Diffeo, Inc.
'''

import os

available_languages = [
    'ar',
    'ca',
    'cs',
    'de',
    'el',
    'en',
    'es',
    'fi',
    'fr',
    'hu',
    'it',
    'ja',
    'kr',
    'nl',
    'no',
    'pl',
    'pt',
    'ru',
    'sk',
    'sv',
    'tr',
    'zh',
    ]

def get_stop_words(*lang_codes):
    '''Returns a set of strings that are stop words for every language
    code in `lang_codes`.  If not language codes are specified, then
    all stop words are returned.

    '''
    if len(lang_codes) == 0:
        lang_codes = available_languages

    stop_words = set()
    for lang_code in lang_codes:
        for line in _open_stop_words_file(lang_code):
            stop_words.add(line.strip())
    return stop_words

def _open_stop_words_file(lang_code):
    this_dir = os.path.dirname(__file__)
    path = os.path.join(this_dir, 'stopwords-{}.txt'.format(lang_code))
    return open(path)
