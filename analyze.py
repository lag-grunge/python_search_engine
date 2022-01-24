import re
import string
import Stemmer

STOPWORDS = set(['и',
'в',
'не',
'на',
'я',
'быть',
'он',
'с',
'что',
'а',
'по',
'это',
'она',
'этот',
'к',
'но',
'они',
'мы',
'как',
'из',
'у',
'который',
'то',
'за',
'свой',
'что',
'весь',
'год',
'от',
'так',
'о',
'для',
'ты',
'же',
'все',
'тот',
'мочь',
'вы',
'человек',
'такой',
'его',
'сказать',
'только',
'или',
'ещё',
'бы',
'себя',
'один',
'как',
'уже',
'до',
'время',
'если',
'сам',
'когда',
'другой',
'вот',
'говорить',
'наш',
'мой',
'знать',
'стать',
'при',
'чтобы',
'дело',
'жизнь',
'кто',
'первый',
'очень',
'два',
'день',
'её',
'новый',
'рука',
'даже',
'во',
'со',
'раз',
'где',
'там',
'под',
'можно',
'ну',
'какой',
'после',
'их',
'работа',
'без',
'самый',
'потом',
'надо',
'хотеть',
'ли',
'слово',
'идти',
'большой',
'должен',
'место',
'иметь',
'ничто'])
PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STEMMER = Stemmer.Stemmer('russian')

def tokenize(text):
    return text.split()

def lowercase_filter(tokens):
    return [token.lower() for token in tokens]

def punctuation_filter(tokens):
    return [PUNCTUATION.sub('', token) for token in tokens]

def stopword_filter(tokens):
    return [token for token in tokens if token not in STOPWORDS]

def stem_filter(tokens):
    return STEMMER.stemWords(tokens)

def analyze(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)
    return [token for token in tokens if token]