from loadpages import loadpages

if __name__=='__main__':
    a = loadpages()
    for i in a[:100]:
        print(i.id, i.created_date)


