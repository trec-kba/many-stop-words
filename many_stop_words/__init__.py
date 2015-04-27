'''many_stop_words has lists of stop words in many languages

.. This software is released under an MIT/X11 open source license.
   Copyright 2012-2015 Diffeo, Inc.

.. autofunction:: get_stop_words
.. autodata:: available_languages

'''
from __future__ import absolute_import, division, print_function
import codecs
import os

#: A default list of languages for :func:`get_stop_words`.
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
    '''Get a set of words that should generally be ignored.

    Returns a set of strings that are stop words for every
    (two-letter, lowercase) language code passed as a positional
    parameter.  If no parameters are specified, then the returned set
    includes all languages for which data is available, listed out in
    :data:`available_languages`.

    '''
    if len(lang_codes) == 0:
        lang_codes = available_languages

    this_dir = os.path.dirname(__file__)

    stop_words = set()
    for lang_code in lang_codes:
        path = os.path.join(this_dir, 'stopwords-{0}.txt'.format(lang_code))
        with codecs.open(path, 'r', 'utf-8-sig') as f:
            for line in f:
                stop_words.add(line.strip())
    return stop_words
