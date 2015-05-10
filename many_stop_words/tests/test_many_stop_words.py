'''tests for many_stop_words

.. This software is released under an MIT/X11 open source license.
   Copyright 2012-2015 Diffeo, Inc.
'''
from __future__ import absolute_import, division, print_function
import pytest
import timeit

from many_stop_words import get_stop_words, available_languages


@pytest.yield_fixture(params=available_languages)
def lang_code(request):
    '''Yields each of the available languages
    '''
    yield request.param


def test_get_one(lang_code):
    stop_words = get_stop_words(lang_code)
    for word in stop_words:
        assert isinstance(word, unicode)
        assert u'\uFEFF' not in word
    assert len(stop_words) > 0


def test_get_two():
    stop_words = get_stop_words('en', 'it')
    assert 'been' in stop_words  # English
    assert 'buono' in stop_words  # Italian
    assert 'bardzo' not in stop_words  # Polish


def test_get_all_basic():
    stop_words = get_stop_words()
    assert 'if' in stop_words


def test_get_all_equals_getting_all():
    assert get_stop_words() == get_stop_words(*available_languages)


def test_load_speed():
    setup = 'from many_stop_words import get_stop_words'
    cmd = 'get_stop_words()'
    number = 100
    t = timeit.timeit(cmd, setup=setup, number=number)
    print('%d in %f seconds --> %f per load' % (number, t, t/number))
    # test_load_speed 100 in 2.074782 seconds --> 0.020748 per load

