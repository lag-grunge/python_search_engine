from dataclasses import dataclass
from collections import Counter
from analysis import analyze
import datetime

class Page:
    def analyze(self):
        self.term_frequencies = Counter(analyze(self.text))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)

    def __init__(self, id, rubrics, text, created_date):
        self.id = id
        self.rubrics = rubrics
        self.text = text
        self.created_date = created_date

    def __str__(self):
        return (str(self.id) + ' ' + str(self.created_date) +'\n' + self.rubrics + '\n' + self.text)





