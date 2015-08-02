import time
from imagga import ImaggaClient

class TagsScore(object):
    def __init__(self):
        pass

    def get_score(self):
        # get the benchmark
        tags_benchmark = open('industries/automotive/tags.csv')
        tags = []
        for tag in tags_benchmark:
            item = tag.rstrip('\n').split(',')
            d = {'tag': item[0], 'benchmark': int(item[1])}
            tags.append(d) 
        print tags 

        # get the list of images
        images = open('results/automotive/images.csv')
        for image_link in images:
            links = image_link.split(',')
            
        # get response from imagga
        imagga_tags = []
        for link in links:
            print 'getting tags for '+link
            link = link.rstrip('\n')
            imagga = ImaggaClient()
            imagga_tags.append(imagga.get_results(link))
            # delay 1 second before sending another request
            time.sleep(1)
        
        # now check whether the tag over the benchmarks
        scores = []
        for imagga_tag in imagga_tags:
            count = 0
            print imagga_tag
            for items in imagga_tag.results[0].tags:
                for tag in tags:
                    if items.confidence >= tag['benchmark'] and items.tag == tag['tag']:
                        print items.tag
                        count = count + 1
            tags_score = int(count) / float(len(tags))
            print tags_score
            scores.append(tags_score)

        average = sum(scores)/float(len(scores))
        return  float(average)

