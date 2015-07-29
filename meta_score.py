import os

class MetaScore(object):
    def __init__(self):
        pass

    def get_score(self):
#        base_dir = os.path.abspath(__file__)

        search_terms = open('industries/automotive/search_terms.csv')
#        search_terms = open(base_dir + '/industries/automotive/search_terms.csv')
        p = 0
        terms = []
        for term in search_terms:
            terms.append(term)
            p = p+1
            
        meta_keywords = open('results/automotive/meta.csv')
        count = 0
        for keyword in meta_keywords:
            words = keyword.split(',')

        for word in words:
            for term in terms:
                if term == word:
                    count = count + 1

        meta_score = int(count) / float(len(terms))
        return  float(meta_score)
