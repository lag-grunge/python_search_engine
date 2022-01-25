from dataclasses import dataclass
from collections import Counter
from analysis import analyze
import datetime

@dataclass
class Page:
    id: int
    rubrics: str
    text: str
    created_date: datetime.datetime

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.text))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)

    def __str__(self):
        return (str(self.id) + ' ' + str(self.created_date) +'\n' + self.rubrics + '\n' + self.text)






