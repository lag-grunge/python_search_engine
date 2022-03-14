import re
import string
from nltk.stem.snowball import SnowballStemmer


PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STEMMER = SnowballStemmer("russian", ignore_stopwords=True)


def tokenize(text):
    return text.split()


def lowercase_filter(tokens):
    return [token.lower() for token in tokens]


def punctuation_filter(tokens):
    return [PUNCTUATION.sub('', token) for token in tokens]

def stem_filter(tokens):
    return [STEMMER.stem(token) for token in tokens if token and token not in STEMMER.stopwords]


def analyze(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = [token for token in tokens if token not in STEMMER.stopwords]
    return tokens

def analyze_all(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = [token if token not in STEMMER.stopwords else None for token in tokens]
    return tokens
