import io
import csv
from page import Page

def loadpages(sizecorp, file='posts.csv'):
    result = []
    with io.open(file, mode='r', encoding='utf-8', newline='') as f:
        f.readline()
        pagereader = csv.reader(f, delimiter=',')
        for (id, row) in enumerate(pagereader):
            result.append(Page(id=id, rubrics=row[2], text=row[0], created_date=row[1]))
            if id == sizecorp - 1:
                break
    return result