
import pytest

from many_stop_words import get_stop_words, available_languages

@pytest.yield_fixture(params=available_languages)
def lang_code(request):
    '''Yields each of the available languages
    '''
    yield request.param


def test_get_one(lang_code):
    stop_words = get_stop_words(lang_code)
    assert len(stop_words) > 0

def test_get_two():
    stop_words = get_stop_words('en', 'it')
    assert len(stop_words) > 0

def test_get_all_basic():
    stop_words = get_stop_words()
    assert len(stop_words) > 0
    assert 'if' in stop_words

def test_get_all_equals_getting_all():
    assert get_stop_words() == get_stop_words(*available_languages)
