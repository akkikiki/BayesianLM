# coding: utf-8

import codecs

def read_corpus():
    corpus = ["data/sample1.txt", "data/sample2.txt"]
    # initialization of a 2D array
    documents = [[] for i in range(len(corpus))]
    #print documents
    for i in range(len(corpus)):
        corpora = corpus[i]
        f = codecs.open(corpora, 'r')
        for line in f:
            documents[i].extend(line[:-1].split(' '))
    print documents
    
    #for n, t in enumerate(documents):
    #    print n, t
    return documents
         
if __name__ == "__main__":
    read_corpus()
