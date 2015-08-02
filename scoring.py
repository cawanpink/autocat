from meta_score import MetaScore
from tags_score import TagsScore



def get_domain_score(image_score, meta_score):
    print '==============='
    print 'meta keyword score: ' + str(meta_score)
    print 'images score: ' + str(image_score)
    return 0.7 * float(image_score) + 0.3 * float(meta_score)


m = MetaScore()
meta_score = m.get_score()

t = TagsScore()
image_score = t.get_score()
print 'DOMAIN SCORE: ' + str(get_domain_score(image_score, meta_score))
