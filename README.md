Many Stop Words
===============

Simple Python package that provides a single function for loading sets
of stop words for different languages.

Stop words in English, French, German, Finish, Hungarian, Turkish,
Russian, Czech, Greek, Arabic, Chinese, Japanese, Korean, Catalan, Polish, Hebrew, Norwegian,
Swedish, Italian, Portuguese and Spanish, were retrieved from the
following sources:

 * Wiktionary lists of prepositions in the respective languages
 * Perseus: http://www.perseus.tufts.edu/hopper/stopwords
 * Ranks.nl: http://www.ranks.nl/resources/stopwords.html
 * Google: http://code.google.com/p/stop-words/
 * Kevin Bouge: https://sites.google.com/site/kevinbouge/stopwords-lists
 * NLTK

The directory called `orig` contains the original files used to
compile the stop word lists.  The directory called `not_used` contains
raw data for creating more stop words lists for languages that are not
yet available in `many_stop_words.available_languages`