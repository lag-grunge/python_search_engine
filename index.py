from page import Page

def indexpages(listpages: list[Page]):
    index = {}
    for p in listpages:
        for token in analyze(p.text):
            if token in index:

    #
    return index
