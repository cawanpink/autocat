import Imagga
import urllib2
import base64
from pprint import pprint

class ImaggaClient(object):

    def __init__(self):
        pass

    def get_api_client(self):
        # initialize the API client
        api_client = Imagga.swagger.ApiClient(api_server="https://api.imagga.com/v1")
        # authentication setting using user name and password
        api_client.username = 'acc_3c47e4992e6a865'
        api_client.password = '05aea6cc7c48cf55c00e61b027691058'
        return api_client

    def get_results(self, url):
        api_client = self.get_api_client()

        try:
            tagging_api = Imagga.TaggingApi(api_client)
            response = tagging_api.tagging(url=url)
            return self.format_response(response)

        except urllib2.HTTPError, e:
            print('[HTTP Error {}]: {}'.format(e.code, e.reason))
            print('Request URL: {}'.format(e.geturl()))
            print('Response body: {}'.format(e.read()))
        except urllib2.URLError, e:
            print('[URL Error]: {}'.format(e.reason))
        except Exception, e:
            print(e)

    @staticmethod
    def format_response(response):
#        new_tags = []
#        print response['results']
#        for items in response['results'][0]['tags']:
#            if items['confidence'] > 5:
#                new_tags.append(items)  
#        response['results'][0].update({'tags': new_tags})
        return response


#url = 'http://www.toyota.com/content/common/img/jellies/global-nav/2015/camry/base.png'
#i = ImaggaClient()
#r = i.get_results(url)
#print r.results[0].tags
