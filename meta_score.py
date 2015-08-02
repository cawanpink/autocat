import os
import re

class MetaScore(object):
    def __init__(self):
        pass

    def get_score(self):
#        base_dir = os.path.abspath(__file__)

        search_terms = open('industries/automotive/search_terms.csv')
#        search_terms = open(base_dir + '/industries/automotive/search_terms.csv')
        terms = []
        for term in search_terms:
            terms.append(term)
            
        meta_keywords = open('results/automotive/meta.csv')
        count = 0
        for keyword in meta_keywords:
            words = keyword.split(',')

        for word in words:
            for term in terms:
                term = term.lower().rstrip('\n')
                word = word.lower().rstrip('\n')
                if term in word:
                    print 'term: ' + term, 'keyword: '+ word
                    count = count + 1
        
        print count, len(terms)
        meta_score = int(count) / float(len(terms))
        return  float(meta_score)
