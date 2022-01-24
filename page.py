from dataclasses import dataclass
import datetime

@dataclass
class Page:
    id: int
    rubrics: str
    text: str
    created_date: datetime.datetime

    def __str__(self):
        return (str(self.id) + ' ' + str(self.created_date) +'\n' + self.rubrics + '\n' + self.text)






