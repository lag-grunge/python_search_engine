from dataclasses import dataclass
from analysis import analyze, analyze_all
from index import Index
from page import Page

sizequery = 10

class Query(object):
    query: str
    ranking: bool
    index: Index
    analyze_query: list
    res: dict
    analyze_res: list
    all_len: int
    show_len: int
    show_start: int
    show_prev: int
    show_next: int


    def __init__(self, query: str, index : Index, ranking=False):
        self.query = query
        self.ranking = ranking
        self.analyze_query = analyze(query)
        self.index = index
        self.res = search(query, index.index, index.pages, ranking=self.ranking)
        if not self.res:
            self.res = dict()
        self.all_len = len(self.res)
        self.show_len = sizequery
        self.show_start = 1
        if not self.res:
            self.show_start = 0
        self.show_end = self.all_len if self.show_start + self.show_len > self.all_len else self.show_start + self.show_len - 1
        self.show_prev = None
        self.show_next = None if self.show_start + self.show_len > self.all_len else self.show_start + self.show_len
        if self.res:
            self.analyze_res = {str(self.res[p]): zip(analyze_all(index.pages[self.res[p]].text), index.pages[self.res[p]].text.split()) \
                       for p in range(self.show_start - 1, self.show_end, 1)}

    def set_show_params(self, move):
        if move == 'next':
            if self.show_next:
                self.show_prev = self.show_start
                self.show_start = self.show_next
                self.show_end = self.all_len if self.show_start + self.show_len > self.all_len else self.show_start + self.show_len - 1
                self.show_next = None if self.show_start + self.show_len > self.all_len else self.show_start + self.show_len
        if move == 'prev':
            if self.show_prev:
                self.show_next = self.show_start
                self.show_start = self.show_prev
                self.show_end = self.all_len if self.show_start + self.show_len > self.all_len else self.show_start + self.show_len - 1
                self.show_prev = None if self.show_start == 1 else (1 if self.show_start - self.show_len < 1 else self.show_start - self.show_len)
        if self.res:
            self.analyze_res = {str(self.res[p]): zip(analyze_all(self.index.pages[self.res[p]].text), self.index.pages[self.res[p]].text.split()) \
                            for p in range(self.show_start - 1, self.show_end, 1)}

def rank(self, query, index, pages:set):
    results = []
    if not pages:
        return results
    for doc in pages:
        score = 0.0
        for token in query:
            tf = pages[doc].term_frequencies[token]
            idf = self.inverse_document_frequency(index, pages, token)
            score += tf * idf
        results.append((doc, score))
    return [r[0] for r in sorted(results, key=lambda x: x[1], reverse=True)]

def time_rank(res:set, pages):
    return [r for r in sorted(res, key=lambda x: pages[x].created_date, reverse=True)]

def search(query, index, pages:set, ranking=False):
    if not query:
        return
    res = set(pages)
    query = query.encode().decode()
    query = analyze(query)
    if not query:
        print("Either empty query or all words in stopwords list")
    if ranking:
        res = rank(query, index, pages)
    else:
        for word in query:
            res = res.intersection(set([p for p in pages if word in analyze(pages[p].text)]))
        if res:
            res = time_rank(res, pages)
    if len(res):
        return res
    return None
