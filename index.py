from math import log10
from analysis import analyze
from page import Page

class Index:
    loadpgs: list
    pages: dict
    index: dict

    def __init__(self,  listpages: list):
        self.loadpgs = listpages
        self.pages = dict()
        self.index = dict()
        for p in listpages:
            if p and p.id not in self.pages:
                self.pages[p.id] = p
                p.analyze()
            for token in analyze(p.text):
                if token not in self.index:
                    self.index[token] = set()
                self.index[token].add(p.id)

def document_frequency(index : dict, token):
    return len(index.get(token, set()))

def inverse_document_frequency(index, pages, token):
    return log10(len(pages) / document_frequency(index, token))