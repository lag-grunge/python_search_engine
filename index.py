from math import log10

from analysis import analyze
from page import Page


def indexpages(listpages:list[Page]):
    index = {}
    pages = {}
    for p in listpages:
        if p and p.id not in pages:
            pages[p.id] = p
            p.analyze()
        for token in analyze(p.text):
            if token not in index:
                index[token] = set()
            index[token].add(p.id)
    return (index, pages)

def document_frequency(index : dict, token):
    return len(index.get(token, set()))


def inverse_document_frequency(index, pages, token):
    return log10(len(pages) / document_frequency(index, token))

def rank(query, index, pages:set[Page]):
    results = []
    if not pages:
        return results
    for doc in pages:
        score = 0.0
        for token in query:
            tf = pages[doc].term_frequencies[token]
            idf = inverse_document_frequency(index, pages, token)
            score += tf * idf
        results.append((doc, score))
    return [r[0] for r in sorted(results, key=lambda x: x[1], reverse=True)]

def time_rank(res:set[Page], pages):
    return [r for r in sorted(res, key=lambda x: pages[x].created_date, reverse=True)]

def search(query, index, pages:set[Page], ranking=False):
    res = set(pages)
    query = analyze(query)
    if not query:
        print("Either empty query or all words in stopwords list")
    if ranking:
        res = rank(query, index, pages)
    else:
        for word in query:
            res = res.intersection(set([p for p in pages if word in pages[p].text]))
        res = time_rank(res, pages)
    for r in res:
        yield r