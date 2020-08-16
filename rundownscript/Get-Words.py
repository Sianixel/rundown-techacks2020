from scholarly import scholarly 
import sys
import requests
import scrapy

class Rundown:

    def __init__(self, keywords):
        self.keywords = keywords

    def get_root(self, key):
        root_article = scholarly.search_pubs(key)
        return(next(root_article).fill())
    
    def extract_abstract(self, root):
        article = getattr(root, 'bib')
        abstract = article['abstract']
        title = article['title']
        return(abstract)

    def get_cited(self, cited_url): 
        scholarly.search_pubs_custom_url(cited_url)
        return(cited)

    def get_citedby(self, pub): 
        #[citation.bib['title'] for citation in pub.citedby]).encode('utf-8').decode('unicode_escape')
        print(pub.citedby)

    def proxy(self):
        proxy_works = scholarly.use_proxy(http="http://29ea0d9d66134811b51ead72601a1181:@proxy.crawlera.com:8010/")
        print(proxy_works)
        
        test_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
        print(test_query)

    def main(self):
        self.proxy()
        #root = self.get_root(self.keywords)
        #abstract = self.extract_abstract(root)
        #citedby = self.get_citedby(root)

        #return(root)

test = Rundown("Agricultural machinery path planning")
output = test.main()

print(output)

#print("åäö".encode('utf-8').decode('unicode_escape'))






